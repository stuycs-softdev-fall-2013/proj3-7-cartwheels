$(function () {
    "use strict";

    var $mainContent = $('.main-content'),
        $manager = $('#cart-manager'),
        $reviews = $('.reviews'),
        $link = $('.cart-link'),
        $addLink = $('.add-link'),
        $addForm = $('#add-form');

    //Initialization
    imagesLoaded($manager, function () {
        resizeImages($manager.get(0), 100);
    });

    $manager.find('#manager-container').width($('.manage-item').length * 350);

    var destroyForm = function (e) {
        e.preventDefault();

        $manager.fadeIn(0);
        $addLink.fadeIn(0);
        $reviews.fadeIn(0);

        $mainContent.find('#info-form').remove();
        $mainContent.find('.links').remove();
    };

    var createForm = function (data) {
        var datum = data.results[0];

        //Form
        var $formDiv = $('<div></div>'),
            $formHeader = $('<div></div>'),
            $form = $('<form></form>'),
            $formErrors = $('<div></div>');

        $formDiv.addClass('form hidden');
        $formDiv.attr('id', 'info-form');
        $formHeader.addClass('form-header');
        $formHeader.text('Manage Cart ' + datum.permit_number);
        $form.attr('method', 'POST');
        $formErrors.addClass('form-errors');

        var $nameInput = $('<input type=text name="name">'),
            $zipInput = $('<input type=text name="zip">'),
            $hiddenInput = $('<input type=hidden name="license">'),
            $submit = $('<input type=submit>');
        
        $nameInput.addClass('input form-input required');
        $nameInput.attr('placeholder', 'Name of cart');
        $nameInput.val(datum.name);

        $zipInput.addClass('input form-input required');
        $zipInput.attr('placeholder', 'Zip code of cart');
        $zipInput.val(datum.zip_code);

        $hiddenInput.val(datum.permit_number);

        $submit.val('submit');

        $form.append($nameInput);
        $form.append($zipInput);
        $form.append($hiddenInput);
        $form.append($submit);

        $formDiv.append($formHeader);
        $formDiv.append($form);
        $formDiv.append($formErrors);

        //Links
        var $linkDiv = $('<div></div>'),
            $viewLink = $('<a href=#></a>'),
            $adLink = $('<a href=#></a>'),
            $menuLink = $('<a href=#></a>'),
            $backLink = $('<a href=#></a>');

        $linkDiv.addClass('links');

        $viewLink.text('View cart page');
        $adLink.text('Buy ads for this cart');
        $menuLink.text('Update menu items');
        $backLink.text('Return to manager');

        $viewLink.attr('href', datum.url_path);
        $menuLink.attr('href', datum.url_path + '/menu');

        $linkDiv.append($viewLink);
        $linkDiv.append('<br>');
        $linkDiv.append($menuLink);
        $linkDiv.append('<br>');
        $linkDiv.append($adLink);
        $linkDiv.append('<br>');
        $linkDiv.append($backLink);

        //Adding nodes
        $mainContent.append($formDiv);
        $mainContent.append($linkDiv);

        $backLink.click(destroyForm);

        //Bind events to the form from form utils
        bindForm();
    };

    var displayForm = function (e) {
        var $this = $(this),
            $manageItem = $this.parent().parent();

        $manager.fadeOut(0);
        $addLink.fadeOut(0);
        $reviews.fadeOut(0);
        $addForm.fadeOut(0);

        //Populate main-content with form
        $.getJSON('/_serve', {'item_type': 'cart', 'permit_number': $manageItem.find('.license').text().trim()}, createForm);
    };

    $link.click(displayForm);

    $addLink.click(function (e) {
        e.preventDefault();

        $addForm.slideToggle();
    });
});
