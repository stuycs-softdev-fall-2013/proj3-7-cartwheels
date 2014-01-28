function bindForm() {
    "use strict";

    var $submit = $('input[type="submit"]');

    //Verify form before submitting
    var formSubmit = function (e) {
        e.preventDefault();
        console.log('here');

        var $this = $(this.parentNode),
            $requiredFields = $this.find('.required'),
            $errors = $('.form-errors'),
            okaySubmit = true;

        //Check if all required fields are filled out
        $.each($requiredFields, function (index, datum) {
            if ($(datum).val() == '') {
                $errors.text('Some required fields were left blank');
                okaySubmit = false;
                return 0;
            }
        });

        if (okaySubmit) {
            $this.submit();
        }
    };

    $submit.on('click', formSubmit);

}
$(function () {
    "use strict";

    bindForm();
});
