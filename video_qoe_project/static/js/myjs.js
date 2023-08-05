function onPageLoad() {
    $(".allSection").hide();
    $(".firstTimeLoad").show();
    $(".optionList").addClass("hidden")
}

function preventReload(formElementSelector, formButtonSelector) {

    var isSubmitting = false
    $("#" + formButtonSelector).click(function () {
        $("#" + formElementSelector).find("input[type='radio']").removeClass('changed-input')
        isSubmitting = true
    })

    $("#" + formElementSelector).on('change keyup keydown', 'input, select', function (e) {
        $(this).addClass('changed-input');
    });

    $(window).on('beforeunload', function () {
        if ($('.changed-input').length && !isSubmitting) {
            return 'You haven\'t saved your changes.';
        }
    });
}


function isHidden(el) {
    var style = window.getComputedStyle(el);
    // return ((style.display === 'none') || (style.visibility === 'hidden'))
    return ((style.display === 'none'));
}

function videoFinishedPlaying() {
    // Get all elements on the page (change this to another DOM element if you want)
    var all = document.getElementsByTagName("section");
    var visible_video = "";


    for (var i = 0, max = all.length; i < max; i++) {
        if (isHidden(all[i])) {
            //console.log(all[i])
            console.log("Element is hidden");
        } else {
            console.log("Element is visible");

            var hidden_section_part = all[i].querySelectorAll(".hidden");
            var hidden_section_part_length = hidden_section_part.length -1;
            var visible_video = all[i].querySelector("video");
            //console.log("inside return " + visible_video)

            visible_video.onended = function () {
                console.log("inside onended");
                console.log(visible_video);
                console.log(hidden_section_part);
                console.log(hidden_section_part_length);
                if (this.played.end(0) - this.played.start(0) === this.duration) {
                    console.log("Played all");
                    for(var i = 0; i <= hidden_section_part_length; i++){
                         hidden_section_part[i].classList.remove("hidden");
                    }
                } else {
                    console.log("Some parts were skipped");
                }
            }
            //console.log(played_all);
            return;
        }
    }
}


$(document).ready(function () {
    onPageLoad();
    $(".allSection button.next_button").click(function () {
        $(".allSection").hide();
        if ($(this).closest("section.allSection").is(':last-child'))
            $('.firstTimeLoad').show();
        else
            $(this).closest("section.allSection").next().show().animate({opacity: 1.0}, "fast");
            videoFinishedPlaying();
    });

    $("section.allSection").find("input[type='radio']").change(function () {
        if ($(".firstTimeLoad").css('display') == 'none' || $(".firstTimeLoad").css("visibility") == "hidden") {
            var section_id = $("section.allSection:visible").find("input[type='radio']")
            var names = {}
            section_id.each(function () {
                names[$(this).attr('name')] = true;
                name = $(this).attr("name");
                console.log(name);
            });

            var count = 0;
            $.each(names, function () { // then count them
                count++;
                console.log(count);
            });

            if ($("section.allSection:visible").find("input[type='radio']:checked").length == count) {

                // all questions answered
                var button_in_section = $("section.allSection:visible").find("button");
                $("section.allSection:visible").find("button").removeAttr("disabled");
            } else {
                console.log("not here");
            }
        }
    });

    questionnaire_form_id = "questionnaire_form"
    survey_form_id = "survey_form"
    questionnaire_button_id = "questionnaire_submit_button"
    survey_button_id = "survey_submit_button"
    endForm_class = "endForm_class"
    endForm_id = "endForm_id"

    preventReload(questionnaire_form_id, questionnaire_button_id);
    preventReload(survey_form_id, survey_button_id);
    preventReload(endForm_id, endForm_class);
});

