function onPageLoad() {
    $(".allSection").hide();
    $(".firstTimeLoad").show();
    // add hidden class to form and button, will need to use thier classes
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

// In Pure JS
// function videoFinishedPlaying(el) {
//      console.log("Inside videoFinishedPlaying function");
//     const videoList = document.querySelectorAll(el); // ".allSection video" use only video when calling this fum=nction for it to work
//     for (let i = 0; i < videoList.length; i++) {
//         //if (!!(element.offsetWidth || element.offsetHeight || element.getClientRects().length)) {
//           //return !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
//         if ( $(el).css('display') != 'none' || $(el).css("visibility") != "hidden"){
//             console.log("visible")
//             document.querySelector(el).onended = function () {
//                 if (this.played.end(0) - this.played.start(0) === this.duration) {
//                     console.log("Played all");
//                 } else {
//                     console.log("Some parts were skipped");
//                 }
//             }
//         }
//
//     }
//
// }


function isHidden(el) {
    var style = window.getComputedStyle(el);
    return ((style.display === 'none') || (style.visibility === 'hidden'))
}

function videoFinishedPlaying() {
    // Get all elements on the page (change this to another DOM element if you want)
    var all = document.getElementsByTagName("section");
    var visible_video = "";
    var played_all = false


    for (var i = 0, max = all.length; i < max; i++) {
        if (isHidden(all[i])) {
            //console.log(all[i])
            console.log("hidden")
        } else {
            console.log("visible " + all[i].querySelector("video"))
            visible_video = all[i].querySelector("video")
            console.log("inside return " + visible_video)

            visible_video.onended = function () {
            console.log("inside onended")
            console.log(visible_video)
            if (this.played.end(0) - this.played.start(0) === this.duration) {
                console.log("Played all");
                played_all = true
                console.log(played_all);
            } else {
                console.log("Some parts were skipped");
            }
        }
            return played_all;
        }
        // console.log("outside onended" + visible_video)
        // visible_video.onended = function () {
        //     console.log("inside onended")
        //     if (this.played.end(0) - this.played.start(0) === this.duration) {
        //         console.log("Played all");
        //     } else {
        //         console.log("Some parts were skipped");
        //     }
        // }

        //console.log(all[i])
        // console.log(i)

        // document.querySelector("video").onended = function () {
        //     if (this.played.end(0) - this.played.start(0) === this.duration) {
        //         console.log("Played all");
        //     } else {
        //         console.log("Some parts were skipped");
        //     }
        // }
    }

    // const videoList = document.querySelectorAll(el); // ".allSection video"
    // for (let i = 0; i < videoList.length; i++) {
    //     //if (!!(element.offsetWidth || element.offsetHeight || element.getClientRects().length)) {
    //       //return !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
    //     if ( $(el).css('display') != 'none' || $(el).css("visibility") != "hidden"){
    //         console.log("visible")
    //         document.querySelector(el).onended = function () {
    //             if (this.played.end(0) - this.played.start(0) === this.duration) {
    //                 console.log("Played all");
    //             } else {
    //                 console.log("Some parts were skipped");
    //             }
    //         }
    //     }
    //
    // }

}


// document.addEventListener("DOMContentLoaded", () => {
//     //let elem = document.querySelector(".allSection video");
//     videoFinishedPlaying("video")
// });


$(document).ready(function () {
    onPageLoad();
    $(".allSection button.next_button").click(function () {
        $(".allSection").hide();

        if ($(this).closest("section.allSection").is(':last-child'))
            $('.firstTimeLoad').show();
        else
            $(this).closest("section.allSection").next().show().animate({opacity: 1.0}, "fast");
        videoFinishedPlaying()  //if it returns true, get form and next button and make them visible

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
                console.log(count)
            });

            if ($("section.allSection:visible").find("input[type='radio']:checked").length == count) {

                // all questions answered
                var button_in_section = $("section.allSection:visible").find("button")
                $("section.allSection:visible").find("button").removeAttr("disabled")
            } else {
                console.log("not here")
            }
        }
    });

    questionnaire_form_id = "questionnaire_form"
    survey_form_id = "survey_form"
    questionnaire_button_id = "questionnaire_submit_button"
    survey_button_id = "survey_submit_button"

    preventReload(questionnaire_form_id, questionnaire_button_id);
    preventReload(survey_form_id, survey_button_id);


});

