$(function () {
    "use strict";

    var $inputBox = $('#search-input'),
        $inputText = $inputBox.find('input'),
        $mainContent = $('.main-content'),
        $prevPage = $('.prev-page'),
        $nextPage = $('.next-page');

    //Constants
    var targetImgHeight = 75,
        searchOffset = 0;

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
        $mainContent.prepend($searchResults);

        //Determine when to display 'next page' and 'previous page'
        if (searchOffset > 0) {
            $prevPage.removeClass('hidden');
        }
        if (data.results.length >= 20) {
            $nextPage.removeClass('hidden');
        }

        resizeImages($mainContent.get(0), targetImgHeight);
        borderLast();
    };

    //When the search term is submitted
    var onInputSubmit = function (offset) {
        //Clear the main content
        $mainContent.find('ul').empty();
        $mainContent.addClass('middle-bar');

        $prevPage.addClass('hidden');
        $nextPage.addClass('hidden');
        
        $(window).scrollTop(0);

        //Grab the values from the fields
        var kwds = $inputBox.find('#kwds').val(),
            loc = $inputBox.find('#loc').val();

        //AJAX request and create html
        $.getJSON('/_data', {'item_type': 'cart', 'keywords': kwds, 'location': loc, 'offset': offset * 20}, createSearchResults);
    };

    var onInputKeypress = function (e) {
        if (e.keyCode === 13) {
            searchOffset = 0;
            onInputSubmit(searchOffset);
        }
    };

    //other initialization
    onInputSubmit(0);

    //event bindings
    $inputText.on('keypress', onInputKeypress);

    $prevPage.click(function (e) {
        searchOffset -= 1;
        onInputSubmit(searchOffset);
    });

    $nextPage.click(function (e) {
        searchOffset += 1;
        onInputSubmit(searchOffset);
    });
});
