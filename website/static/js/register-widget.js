$(function () {
    "use strict";

    var $toggleInfo = $('.toggle-desc');

    //Toggle displaying of extra information
    var toggleDescription = function (e) {
        var $this = $(this),
            $info = $this.parent().find('.description');
        
        console.log(this.parentNode);

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
