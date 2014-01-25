function resizeImages(node, targetImgHeight) {
    "use strict";

    var $node = $(node);
    var imageList = $node.find('img');

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
