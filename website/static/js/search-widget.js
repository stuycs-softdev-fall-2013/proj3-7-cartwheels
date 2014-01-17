$(function () {
    "use strict";

    var $inputBox = $('#search-input'),
        $inputText = $inputBox.find('input'),
        $mainContent = $('.main-content');

    //Constants
    var targetImgHeight = 75;

    //Resize images in the search results
    var resizeImageResults = function () {
        var imageList = $mainContent.find('img');

        imageList.each(function () {
            var $img = $(this);
            var w = (typeof $img.data("width") != 'undefined') ? $img.data("width") : $img.width(),
                h = (typeof $img.data("height") != 'undefined') ? $img.data("height") : $img.height(),
                aspectRatio = w / h,
                nw = aspectRatio * targetImgHeight;

            this.style.height = targetImgHeight + 'px';
            this.style.width = nw + 'px';
        });
    };

    //Add border on last search result
    var borderLast = function () {
        var searchItems = $mainContent.find('.search-item'),
            lastItem = $(searchItems[searchItems.length - 1]);

        lastItem.css({
            'border-bottom': '1px solid #efefef'
        });
    };

    //Create the search results
    var createSearchResults = function (data) {
        console.log(data);
    };

    //When the search term is submitted
    var onInputSubmit = function (e) {
        if (e.keyCode === 13) {
            //Clear the main content
            $mainContent.empty();
            
            $(window).scrollTop(0);

            //Grab the values from the fields
            var kwds = $inputText.find('#kwds').value(),
                loc = $inputText.find('#loc').value();

            //AJAX request and create html
            $.getJSON('/_data', {'item_type': 'cart', 'keywords': kwds, 'location': loc}, createSearchResults);
            resizeImageResults();
            borderLast();
        }
    };

    //event bindings
    $inputText.on('keypress', onInputSubmit);
});
