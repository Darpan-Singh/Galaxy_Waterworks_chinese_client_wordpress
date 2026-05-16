<?php get_header(); ?>
<main class="site-main container" style="padding:120px 24px 80px;">
    <?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
        <article><?php the_content(); ?></article>
    <?php endwhile; endif; ?>
</main>
<?php get_footer(); ?>
