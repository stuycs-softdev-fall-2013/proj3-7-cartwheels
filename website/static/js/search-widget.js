function toTitleCase(str) {
    "use strict";
    return str.replace(/\w\S*/g, function (txt) {return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase(); });
}

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
            var w = (typeof $img.data('width') !== undefined) ? $img.data('width') : $img.width(),
                h = (typeof $img.data('height') !== undefined) ? $img.data('height') : $img.height(),
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

        var $searchResults = $('<ul></ul>');

        $.each(data.results, function (index, datum) {
            var $item = $('<li></li>');
            $item.addClass('centered-relative search-item');

            //add image
            var $imgDiv = $('<div></div>'),
                $img = $('<img>');

            $imgDiv.addClass('image-meta');

            if (datum.image_paths.length > 0) {
                $img.attr('src', datum.image_paths[0]);
            } else {
                $img.attr('src', '/_image-default');
            }

            $imgDiv.append($img);
            $item.append($imgDiv);

            //add content
            var $contentDiv = $('<div></div>'),
                $rating = $('<div></div>'),
                $name = $('<div></div>'),
                $address = $('<div></div>'),
                $link = $('<a></a>');

            $contentDiv.addClass('content-meta');

            $rating.addClass('rating');
            $rating.text(datum.rating);

            $name.addClass('name');
            $name.text(toTitleCase(datum.name));

            $address.addClass('address');
            $address.text(toTitleCase(datum.address));

            $link.addClass('link');
            $link.attr('href', datum.url_path);

            $contentDiv.append($rating)
                .append($name)
                .append($address)
                .append($link);

            $item.append($contentDiv);

            //add tags
            var $tagsDiv = $('<div></div>');
            $.each(datum.tags, function (index, tag) {
                $tagsDiv.append('<span>' + tag + '</span>');
            });

            $item.append($tagsDiv);

            //append item
            $searchResults.append($item);
        });

        $mainContent.append($searchResults);
        resizeImageResults();
        borderLast();
    };

    //When the search term is submitted
    var onInputSubmit = function (e) {
        if (e.keyCode === 13) {
            //Clear the main content
            //Change later to redirect page
            $mainContent.empty();
            
            $(window).scrollTop(0);

            //Grab the values from the fields
            var kwds = $inputBox.find('#kwds').val(),
                loc = $inputBox.find('#loc').val();

            //AJAX request and create html
            $.getJSON('/_data', {'item_type': 'cart', 'keywords': kwds, 'location': loc}, createSearchResults);
        }
    };

    //event bindings
    $inputText.on('keypress', onInputSubmit);
});
