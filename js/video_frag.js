

/*
 * Allow video to be inserted in fragment loop
 */

function playCurrentFragment() {
    [].slice.call( document.querySelectorAll('.fragment') ).forEach(function(fragment) {
        
        if(fragment.tagName == "VIDEO"){
            var video = fragment;
            if(video.classList.contains('current-fragment')) {
                video.currentTime = 0;
                video.play();
            }
            else {
                //video.pause();
            }
        }
    });
}

Reveal.addEventListener( 'fragmentshown', playCurrentFragment );
Reveal.addEventListener( 'fragmenthidden', playCurrentFragment );

