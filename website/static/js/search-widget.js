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

    //Add border on last search result
    var borderLast = function () {
        var searchItems = $mainContent.find('.search-item'),
            lastItem = $(searchItems[searchItems.length - 1]);

        lastItem.css({
            'border-bottom': '1px solid #eee'
        });
    };

    //Create the search results
    var createSearchResults = function (data) {

        var $searchResults = $('<ul></ul>');

        $.each(data.results, function (index, datum) {
            //sanitize data
            if (datum.name == '') {
                datum.name = 'Name Unknown';
            }
            if (datum.zip_code == '') {
                datum.zip_code = 'Zip Code Unknown';
            }
            if (datum.rating == null) {
                datum.rating = 'Rating Not Available';
            }

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
                $zip = $('<div></div>'),
                $link = $('<a>View Page</a>'),
                $tagsDiv = $('<div></div>');

            $contentDiv.addClass('content-meta');

            $rating.addClass('rating');
            $rating.text(datum.rating);

            $name.addClass('name');
            $name.text(toTitleCase(datum.name));

            $zip.addClass('zip');
            $zip.text(datum.zip_code);

            $link.addClass('link');
            $link.attr('href', datum.url_path);

            $contentDiv.append($rating)
                .append($name)
                .append($zip)
                .append($link);

            $item.append($contentDiv);

            //add tags
            $tagsDiv.addClass('tags-meta');
            $.each(datum.tags, function (index, tag) {
                $tagsDiv.append('<span>' + tag + '</span>');
            });

            $item.append($tagsDiv);

            //append item
            $searchResults.append($item);
        });

        $mainContent.append($searchResults);
        resizeImages($mainContent.get(0), targetImgHeight);
        borderLast();
    };

    //When the search term is submitted
    var onInputSubmit = function (e) {
        if (e.keyCode === 13) {
            //Clear the main content
            //Change later to redirect page
            $mainContent.empty();
            $mainContent.addClass('middle-bar');
            
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
