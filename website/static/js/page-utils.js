// Make a string title case
function toTitleCase(str) {
    "use strict";
    return str.replace(/\w\S*/g, function (txt) {return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase(); });
}

//Resize images to a certain height based on their aspect ratios
function resizeImages(node, targetImgHeight) {
    "use strict";

    var $node = $(node),
        imageList = $node.find('img');

    imageList.each(function () {
        var $img = $(this);
        var w = (typeof $img.data('width') !== undefined) ? $img.data('width') : $img.width(),
            h = (typeof $img.data('height') !== undefined) ? $img.data('height') : $img.height(),
            aspectRatio = w / h,
            nw = aspectRatio * targetImgHeight;

        this.style.height = targetImgHeight + 'px';
        this.style.width = nw + 'px';
    });
}

//When the page has loaded
$(function () {
    "use strict";

    var $mainContent = $('.main-content'),
        $inputBox = $('#search-input'),
        $inputText = $inputBox.find('input');

    //Redirect to the search page if not already on it
    var onInputKeypress = function (e) {
        if (e.keyCode === 13 && document.URL.indexOf('/search') === -1) {
            $mainContent.addClass('hidden');

            //Grab the values from the fields
            var kwds = $inputBox.find('#kwds').val(),
                loc = $inputBox.find('#loc').val();

            //Copy the values onto the url
            window.location.href = '/search?kwds=' + kwds + '&loc=' + loc;
        }
    };

    //event bindings
    $inputText.on('keypress', onInputKeypress);
});
