<?php
/* ─────────────────────────────────────────────
   THEME SETUP
───────────────────────────────────────────── */
function galaxy_setup() {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    add_theme_support( 'html5', [
        'search-form', 'comment-form', 'comment-list',
        'gallery', 'caption', 'style', 'script',
    ] );
    add_theme_support( 'align-wide' );
    add_theme_support( 'responsive-embeds' );
    add_theme_support( 'custom-logo' );

    register_nav_menus( [
        'primary' => '主選單',
        'footer'  => '頁尾選單',
    ] );
}
add_action( 'after_setup_theme', 'galaxy_setup' );

/* ─────────────────────────────────────────────
   ENQUEUE CSS + JS  (cache-busting via filemtime)
───────────────────────────────────────────── */
function galaxy_enqueue_assets() {
    $uri = get_template_directory_uri();
    $dir = get_template_directory();

    wp_enqueue_style(
        'galaxy-main',
        $uri . '/assets/css/main.css',
        [],
        filemtime( $dir . '/assets/css/main.css' )
    );

    wp_enqueue_script(
        'galaxy-main',
        $uri . '/assets/js/main.js',
        [],
        filemtime( $dir . '/assets/js/main.js' ),
        true
    );
}
add_action( 'wp_enqueue_scripts', 'galaxy_enqueue_assets' );

/* ─────────────────────────────────────────────
   REMOVE CONFLICTING WORDPRESS DEFAULT STYLES
───────────────────────────────────────────── */
add_action( 'wp_enqueue_scripts', function () {
    wp_dequeue_style( 'wp-block-library' );
    wp_dequeue_style( 'wp-block-library-theme' );
    wp_dequeue_style( 'global-styles' );
    wp_dequeue_style( 'classic-theme-styles' );
}, 100 );

remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );

/* ─────────────────────────────────────────────
   ELEMENTOR COMPATIBILITY
───────────────────────────────────────────── */

// Auto-replace image placeholder URLs when Elementor imports/saves a template
add_filter( 'elementor/document/save/data', function ( $data ) {
    $site_url = rtrim( home_url(), '/' );
    $encoded  = wp_json_encode( $data );
    $encoded  = str_replace( 'REPLACE_WITH_YOUR_SITE_URL', $site_url, $encoded );
    return json_decode( $encoded, true );
} );

// 0. Auto-fix image URLs when Elementor renders template content
add_filter( 'elementor/frontend/the_content', function ( $content ) {
    return str_replace( 'REPLACE_WITH_YOUR_SITE_URL', rtrim( home_url(), '/' ), $content );
} );

// 1. Register Elementor Pro theme builder locations
//    (header, footer, single, archive — lets Elementor Pro override them)
add_action( 'elementor/theme/register_locations', function ( $manager ) {
    $manager->register_all_core_location();
} );

// 2. Load our theme CSS inside the Elementor editor so previews look correct
add_action( 'elementor/editor/after_enqueue_styles', function () {
    wp_enqueue_style(
        'galaxy-main-editor',
        get_template_directory_uri() . '/assets/css/main.css',
        [],
        filemtime( get_template_directory() . '/assets/css/main.css' )
    );
} );

// 3. Load our CSS in Elementor's preview iframe
add_action( 'elementor/preview/enqueue_styles', function () {
    wp_enqueue_style(
        'galaxy-main-preview',
        get_template_directory_uri() . '/assets/css/main.css',
        [],
        filemtime( get_template_directory() . '/assets/css/main.css' )
    );
} );

// 4. Prevent Elementor from overriding our theme colours & fonts
add_action( 'elementor/init', function () {
    update_option( 'elementor_disable_color_schemes',      'yes' );
    update_option( 'elementor_disable_typography_schemes', 'yes' );
} );

// 5. Expose our CSS custom-property colour tokens to Elementor's Global Colours
add_action( 'elementor/editor/footer', function () { ?>
    <style>
        :root {
            --teal:      #5BBCBC;
            --teal-mid:  #3D9898;
            --teal-dark: #2A7474;
            --teal-bg:   #F0FAFA;
            --text:      #1A1A1A;
        }
    </style>
<?php } );

/* ─────────────────────────────────────────────
   AUTO-SETUP ON THEME ACTIVATION
   • creates 首頁 page
   • sets static front page
   • assigns nav menus
───────────────────────────────────────────── */
function galaxy_theme_activation() {

    $homepage = get_page_by_path( 'home' );
    if ( ! $homepage ) {
        $page_id = wp_insert_post( [
            'post_title'   => '首頁',
            'post_name'    => 'home',
            'post_status'  => 'publish',
            'post_type'    => 'page',
            'post_content' => '',
        ] );
    } else {
        $page_id = $homepage->ID;
    }

    update_option( 'show_on_front', 'page' );
    update_option( 'page_on_front', $page_id );

    $primary = get_term_by( 'slug', 'primary-menu', 'nav_menu' );
    $footer  = get_term_by( 'slug', 'footer-menu',  'nav_menu' );

    $locations = [];
    if ( $primary ) $locations['primary'] = $primary->term_id;
    if ( $footer )  $locations['footer']  = $footer->term_id;
    if ( $locations ) set_theme_mod( 'nav_menu_locations', $locations );
}
add_action( 'after_switch_theme', 'galaxy_theme_activation' );
