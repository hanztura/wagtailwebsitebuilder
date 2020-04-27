const io = new IntersectionObserver((entries) =>
    entries.forEach((entry) => {
        // set image source only when it is in the viewport
        if (entry.isIntersecting) {
            const image = entry.target;

            if (image.className.indexOf('hero') >= 0) {
                image.style.backgroundImage = `url(${image.dataset.src})`;
                image.className.indexOf('overlay') >= 0 ? image.style.backgroundBlendMode = 'overlay': false;
            } else {
                // setting image source from the dataset
                image.src = image.dataset.src;
            }

            // when image is loaded, we do not need to observe it any more
            io.unobserve(image);
        }
    })
);

document.querySelectorAll(".lazy").forEach((element) => io.observe(element));
