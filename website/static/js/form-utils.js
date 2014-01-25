$(function () {
    "use strict";
    var $submit = $('input[type="submit"]');

    var formSubmit = function (e) {
        e.preventDefault();

        var $this = $(this.parentNode),
            $requiredFields = $this.find('.required'),
            $errors = $this.parent().find('.form-errors'),
            okaySubmit = true;

        $.each($requiredFields, function (index, datum) {
            if ($(datum).val() == '') {
                console.log('hello');
                if ($errors.hasClass('hidden')) {
                    $errors.removeClass('hidden');
                }

                $errors.text('Some required fields were left empty');
                okaySubmit = false;
                return 0;
            }
        });

        if (okaySubmit) {
            $this.submit();
        }
    };

    $submit.on('click', formSubmit);
});
