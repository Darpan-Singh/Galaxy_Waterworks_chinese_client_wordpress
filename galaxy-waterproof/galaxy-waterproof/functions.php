<?php
function galaxy_setup() {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    add_theme_support( 'html5', [
        'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script'
    ] );
    register_nav_menus( [
        'primary' => '主選單',
        'footer'  => '頁尾選單',
    ] );
}
add_action( 'after_setup_theme', 'galaxy_setup' );

/* Enqueue theme CSS + JS with cache-busting */
function galaxy_enqueue_assets() {
    $theme_uri = get_template_directory_uri();
    $theme_dir = get_template_directory();

    wp_enqueue_style(
        'galaxy-main',
        $theme_uri . '/assets/css/main.css',
        [],
        filemtime( $theme_dir . '/assets/css/main.css' )
    );
    wp_enqueue_script(
        'galaxy-main',
        $theme_uri . '/assets/js/main.js',
        [],
        filemtime( $theme_dir . '/assets/js/main.js' ),
        true
    );
}
add_action( 'wp_enqueue_scripts', 'galaxy_enqueue_assets' );

/* Remove WordPress default styles that conflict */
add_action( 'wp_enqueue_scripts', function () {
    wp_dequeue_style( 'wp-block-library' );
    wp_dequeue_style( 'wp-block-library-theme' );
    wp_dequeue_style( 'global-styles' );
    wp_dequeue_style( 'classic-theme-styles' );
}, 100 );

/* Remove emoji scripts */
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );

/* Auto-setup on theme activation:
   - Create homepage if missing
   - Set static front page
   - Assign nav menus to locations */
function galaxy_theme_activation() {

    // Create or find the homepage
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

    // Set static front page
    update_option( 'show_on_front', 'page' );
    update_option( 'page_on_front', $page_id );

    // Assign nav menus to theme locations
    $primary = get_term_by( 'slug', 'primary-menu', 'nav_menu' );
    $footer  = get_term_by( 'slug', 'footer-menu', 'nav_menu' );

    $locations = [];
    if ( $primary ) $locations['primary'] = $primary->term_id;
    if ( $footer )  $locations['footer']  = $footer->term_id;
    if ( $locations ) set_theme_mod( 'nav_menu_locations', $locations );
}
add_action( 'after_switch_theme', 'galaxy_theme_activation' );
