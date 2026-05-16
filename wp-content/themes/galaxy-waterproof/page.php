<?php
$template = get_page_template_slug();

// Elementor Canvas — no header, no footer, pure blank canvas
if ( 'elementor_canvas' === $template ) {
    while ( have_posts() ) { the_post(); the_content(); }
    wp_footer();
    return;
}

get_header();

// Elementor Full-Width — our header/footer, but no sidebar/padding
if ( 'elementor_header_footer' === $template ) : ?>
    <main id="main">
        <?php while ( have_posts() ) { the_post(); the_content(); } ?>
    </main>
<?php else : ?>
    <main class="site-main container" style="padding:120px 24px 80px;">
        <?php while ( have_posts() ) : the_post(); ?>
            <h1 style="margin-bottom:24px;font-size:clamp(24px,3vw,36px);font-weight:900;color:#1A1A1A;">
                <?php the_title(); ?>
            </h1>
            <?php the_content(); ?>
        <?php endwhile; ?>
    </main>
<?php endif;

get_footer();
