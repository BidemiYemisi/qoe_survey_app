from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import QoeVideo, Respondent, QoeRating, ValidationVideo
from .forms import CreateQuestionnaireForm
import random

# Define GLOBAL variables
respondent_id = 0
playlist = {}
validation_video = ""


# Create your views here.
def welcome_page(request):
    return render(request, 'video_qoe_app/welcome.html')  # specify template name

def questionnaire_page(request):
    global respondent_id
    form = CreateQuestionnaireForm(request.POST or None)
    if request.method == "POST":
        # print(request.POST)
        # create a form instance and populate it with data from the request:
        # form = CreateQuestionnaireForm(request.POST)
        # check whether it's valid:
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        if form.is_valid():
            respondent_age_range = form.cleaned_data['age_range']  # pass cleaned values from form to a variable
            respondent_gender = form.cleaned_data['gender']
            create_respondent = Respondent(age_range=respondent_age_range, gender=respondent_gender)
            create_respondent.save()

            # Try to get ID of newly saved respondent
            try:
                respondent_id = create_respondent.respondent_id
                request.session["respondent_id"] = respondent_id
            except create_respondent.DoesNotExist:
                respondent_id = None
            print("This is resp ID", respondent_id)

            if respondent_id is not None and "respondent_id" in request.session:
                # fetch id of respondent and pass to next page
                # respondant_details = Respondent.objects.all()
                # messages.success(request, 'respondent with id  {}  added.'.format(create_respondent.respondent_id))
                # return redirect("questionnaire")
                return redirect("survey")
            else:
                form = CreateQuestionnaireForm()
                context = {'form': form}
                return render(request, 'video_qoe_app/questionnaire.html', context)

        # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = CreateQuestionnaireForm()
    #     context = {'form': form}
    return render(request, 'video_qoe_app/questionnaire.html', {"form": form})

def get_random_videos_id_from_model():
    random_video_id = random.sample(range(1, 3), 2)  # range(2, 7), 4 //range(1,3) means create numbers from 1 to 2, 3 won't be included
    return random_video_id


def fetch_videos_from_model():
    random_video_ids = get_random_videos_id_from_model()
    # print(type(random_video_ids))
    video_playlist = {}  # Dict
    video_path_list = []  # List
    video_id_list = []  # List
    for random_id in random_video_ids:
        # print("fetch_videos_from_model - this is random number", random_id)
        try:
            video_obj = QoeVideo.objects.get(video_id=random_id)
            video_path = video_obj.video_file_path
            video_id_num = video_obj.video_id
        except QoeVideo.DoesNotExist:
            video_path = None
            video_id_num = None

        video_path_list.append(video_path)
        video_id_list.append(video_id_num)
        # print("fetch_videos_from_model - this is path list", video_path_list)
        # print("fetch_videos_from_model - this is id_num list", video_id_list)

    for i in range(len(video_id_list)):
        video_playlist[video_id_list[i]] = video_path_list[i]
        # print("fetch_videos_from_model - this is dict playlist", video_playlist)
    return video_playlist


def fetch_validation_videos():
    random_validation_video_id = random.randint(1, 4)

    try:
        validation_video_obj = ValidationVideo.objects.get(validation_video_id=random_validation_video_id)
        validation_video_path = validation_video_obj.validation_video_file_path
    except ValidationVideo.DoesNotExist:
        validation_video_path = None

    return validation_video_path


def survey_page(request):
    global playlist
    global validation_video
    error_message = ""
    try:
        respondent_details = Respondent.objects.get(respondent_id=respondent_id)  ##need to look at respondent_details, maybe declare the variable
    except Respondent.DoesNotExist:
        #respondent_details = None
        error_message = "You need to go to home page to start the survey. Please copy this url http://127.0.0.1:8000 and paste in your browser"
        print("inside try catch in survey_page", respondent_id)
        #print(respondent_details)
        return redirect("welcome")

    if request.method == 'POST':
        # print(request.POST)
        if request.POST.get('submit_rating'):  # submit button
            for key, value in playlist.items():
                try:
                    new_rated_video = QoeVideo.objects.get(video_id=key)
                except QoeVideo.DoesNotExist:
                    new_rated_video = None
                    print("Video should be empty", new_rated_video)

                new_rating_perception = request.POST.get('qoe_rating_one_' + str(key))
                new_rating_value = request.POST.get('qoe_rating_two_' + str(key))
                new_validation_video_resp = request.POST.get('validation_question')

                if new_rated_video is None or new_rating_perception is None or new_rating_value is None or new_validation_video_resp is None:
                    error_message = "Not all questions were answered or missing videos. Please go to home page and retake survey"
                    return render(request, 'video_qoe_app/survey.html', {"error_message": error_message})
                # if new_rated_video is not None and new_rating_perception is not None and new_rating_value is not None:
                #     respondent_details.qoerating_set.create(qoe_rating_value=new_rating_value,
                #                                             qoe_rating_perception=new_rating_perception,
                #                                             video=new_rated_video)
                    #return redirect("end")

                else:
                    respondent_details.qoerating_set.create(qoe_rating_value=new_rating_value,
                                                            qoe_rating_perception=new_rating_perception,
                                                            video=new_rated_video,
                                                            respondent_validation_video_anwer=new_validation_video_resp,
                                                            validation_video_path=validation_video)
        return redirect("end")
    else:
        playlist = fetch_videos_from_model()  ##looks like I need to handle the playing of video some else and pass it here
        validation_video = fetch_validation_videos()
        print(playlist)  # get the key of playlist dict and passs it to qoe_rating_one and two keys, also use the key to get the video obj
        print(validation_video)
        context = {'playlist': playlist,
                   'validation_video': validation_video}
        # 'error_message': error_message}
        return render(request, 'video_qoe_app/survey.html', context)

def bye_page(request):
    return render(request, 'video_qoe_app/bye.html')

def end_page(request):
    global respondent_id
    current_respondent_id = request.session.get("respondent_id")
    print("inside end_page", current_respondent_id)
    if request.POST.get("more_rating"):
        rate_more_response = request.POST.get("more_rating")
        if rate_more_response == "Yes":
            respondent_id = request.session["respondent_id"]
            print("respondent_id inside end with Yes response", respondent_id)
            return redirect("survey")
        else:
            try:
                print("Inside Try end_page", request.session["respondent_id"])
                del request.session["respondent_id"]
            except KeyError:
                print("Before Pass in end_page", request.session["respondent_id"])
                pass
            return redirect("bye")
    return render(request, 'video_qoe_app/end.html')



# https://stackoverflow.com/questions/22976662/return-primary-key-after-saving-to-a-model-in-django


