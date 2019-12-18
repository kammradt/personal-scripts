// I will update this using something like Puppeteer,
// At this moment you need to run this code on the console of wanted playlist
// For example: https://www.youtube.com/playlist?list=PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ

document.querySelectorAll("[id='video-title']")
    .forEach(spanTitle => {
        let titleText = spanTitle.innerText

        // this part is not required, just useful sometimes
        let formattedTitle = titleText.replace('Unwanted substring from title ', '').trim()
        console.log(formattedTitle)
    })