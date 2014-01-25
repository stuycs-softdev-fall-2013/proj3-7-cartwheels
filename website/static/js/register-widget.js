$(function () {
    "use strict";

    var $toggleInfo = $('.toggle-desc');

    var toggleDescription = function (e) {
        var $this = $(this.parentNode),
            $info = $this.find('.description');

        if ($info.hasClass('hidden')) {
            $info.slideDown();
            $info.removeClass('hidden');
            $this.text('less information');
        } else {
            $info.slideUp();
            $info.addClass('hidden');
            $this.text('more information');
        }
    };

    $toggleInfo.click(toggleDescription);
});
