
    $(document).ready(function () {
    onPageLoad();

    $("button").click(function () {
    $(".allSection").hide();
    var parent = $('section');
    var element = $(this).parent().is(':last-child');
    if ($(this).parent().is(':last-child'))
    $('.firstTimeLoad').show();
    else
    $(this).parent().next().show();

});

});

    function onPageLoad() {
    $(".allSection").hide();
    $(".firstTimeLoad").show();
}
