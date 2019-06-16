from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question, BEST
from django.utils import timezone
import random
from .forms import Lookfor
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import MarkerForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request):

    if request.method == 'POST':
        form = MarkerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/polls/find')
    else:
        form = MarkerForm()
        latest_question_list = Question.objects.order_by('-pk')
        template = loader.get_template('polls/Find.html')
        context = {
            'latest_question_list': latest_question_list,
            "form": form,
        }
        return HttpResponse(template.render(context, request))


def getbest(request):
    allbestlist = BEST.objects.order_by('-id')
    template = loader.get_template('polls/Best_Quotes.html')
    context = {
        'allbestlist' : allbestlist,
    }
    return HttpResponse(template.render(context,request))


def database(request):
    N = None
    template = loader.get_template('polls/Database.html')
    context = {
        'var': N,
    }
    return HttpResponse(template.render(context, request))

def get_name(request):

    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            template = loader.get_template('polls/look.html')
            user = Question.objects.filter(Quote_text__startswith=search_id)


            user.order_by("-datetime")
            # do something with user
            for question in user:
                pass
            context = {
                'quote':user,

            }
            return HttpResponse(template.render(context,request))
        except Question.DoesNotExist:
            return HttpResponse("no such quote")
    else:
        return render(request, 'Find.html')




def generatequotes(request):
    verbs = ["be", "were", "been", "have", "had", "had", "do", "don't", "did", "done", "say", "said", "said", "go",
             "went", "gone", "get", "got", "got", "gotten", "make", "made", "made", "know", "knew",    "known ",
             "think","thought","thought", "take", "took", "taken", "see", "saw", "seen", "come", "came", "come", "want",
             "wanted","wanted", "look", "looked", "looked", "use", "used", "used", "find", "found", "found", "give",
             "gave", "given", "tell", "told", "told", "work", "worked", "worked", "call", "called", "called", "try",
             "tried", "tried", "ask", "asked", "asked", "need", "needed", "needed", "feel", "felt", "felt",
             "become", "became", "become", "leave", "left", "left", "put", "put", "put", "mean", "meant", "meant",
             "keep", "kept", "kept", "let", "let", "let", "begin", "began", "begun", "seem", "seemed", "seemed", "help",
             "helped", "helped", "talk", "talked", "talked", "turn", "turned", "turned", "start", "started", "started", "show",
             "showed", "shown", "hear", "heard", "heard", "play", "played", "played", "run", "ran", "run", "move",
             "moved", "moved","like", "liked", "liked", "live", "lived", "lived", "believe", "believed", "believed", "hold", "held",
             "held", "bring", "brought", "brought", "happen", "happened", "happened", "write", "wrote", "written",
             "provide", "provided", "provided", "sit", "sat", "sat", "to", "stand", "stood", "stood", "lose", "lost",
             "lost", "pay", "paid", "paid", "meet", "met", "met", "include", "included", "included", "continue",
             "continued", "continued", "set", "set", "set", "learn",
             "learnt", "learned",  "learnt", "learned", "change", "changed", "changed", "lead", "led", "led",
             "understand", "understood", "understood", "watch", "watched", "watched", "follow", "followed", "followed",
             "stop", "stopped", "stopped", "create", "created", "created", "speak",
             "spoke", "spoken", "read", "read", "read", "allow", "allowed", "allowed", "add", "added", "added", "spend",
             "spent", "spent", "grow", "grew", "grown", "open", "opened", "opened", "walk", "walked", "walked", "win",
             "won", "won", "offer", "offered", "offered",
             "remember", "remembered", "remembered", "love", "loved", "loved", "consider", "considered", "considered",
             "appear", "appeared", "appeared", "buy", "bought", "bought", "wait", "waited", "waited", "serve", "served",
             "served", "die", "died", "died", "send", "sent", "sent", "expect", "expected", "expected",
             "build", "built", "built", "stay", "stayed", "stayed", "fall", "fell", "fallen", "cut", "cut", "cut",
             "reach", "reached", "reached", "kill", "killed", "killed", "remain", "remained", "remained", "suggest",
             "suggested", "suggested", "raise", "raised", "raised", "pass", "passed", "passed", "sell", "sold", "sold",
             "require", "required", "required", "report", "reported", "reported", "decide", "decided", "decided",
             "pull", "pulled", "pulled"]

    QUOTES = ["The gem cannot be polished without friction, nor man perfected without trials.",
    "An investment in knowledge always pays the best interest.",
    "Remember, you can earn more money, but time when spent is gone forever. ",
    "The greatest of all weaknesses is the fear of appearing weak."
    "The first requisite of success is the ability to apply your physical and mental energies to one problem without growing weary.",
    "We don't stop playing because we grow old; we grow old because we stop playing.",
    "Great things are not done by impulse, but by a series of small things brought together.",
    "I feel that the greatest reward for doing is the opportunity to do more.",
    "You've got to be before you can do, and do before you can have.",
    "A superior man is modest in his speech, but exceeds in his actions.",
    "Ability will never catch up with the demand for it."
    "No matter how busy you may think you are, you must find time for reading, or surrender yourself to self chosen ignorance.",
    "Our greatest glory is not in never falling, but in rising every time we fall.",
    "Real knowledge is to know the extent of one's ignorance.",
    "Learning without thought is labor lost; thought without learning is perilous.",
    "The only worthwhile achievements of man are those which are socially useful.",
    "God put me on Earth to accomplish a certain number of things.",
    "Lack of direction, not lack of time, is the problem. We all have twenty four hour days."
    "Destiny is not a matter of chance, it is a matter of choice; it is not a thing to be waited for, it is a thing to be achieved.",
    "Unless a man undertakes more than he possibly can do, he will never do all that he can.",
    "The best job goes to the person who can get it done without passing the buck or coming back with excuses.",
    "Only those who dare to fail greatly can ever achieve greatly. ",
    "It is time for us all to stand and cheer for the doer, the achiever the one who recognizes the challenge and does something about it.",
    "The heights by great men reached and kept; Were not obtained by sudden flight; But they, while their companions slept; Were toiling upward in the night.",
    "You don't drown by falling in water; you only drown if you stay there. ",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "Obstacles are things a person sees when he takes his eyes off his goal.",
    "The man who can drive himself further once the effort gets painful is the man who will win.",
    "You'll never achieve your dreams if they don't become goals.",
    "The spirit, the will to win, and the will to excel are the things that endure. These qualities are so much more important than the events that occur.",
    "Lombardi time is the principle that one should arrive 10 to 15 minutes early, or else be considered late.",
    "Every worthwhile accomplishment, big or little, has its stages of drudgery and triumph; a beginning, a struggle and a victory.",
    "The price of success is hard work, dedication to the job at hand, and the determination that whether we win or lose, we have applied the best of ourselves to the task at hand.",
    "A failure establishes only this, that our determination to succeed was not strong enough.",
    "He who has a why to live for can bear almost any how.",
    "A leader, once convinced that a particular course of action is the right one, must....be undaunted when the going gets tough.",
    "It is our attitude at the beginning of a difficult task which, more than anything else, will affect it’s successful outcome.",
    "I'ts not what happens to you that determines how far you will go in life ;it is how you handle what happens to you.",
    "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned.",
    "The optimist sees opportunity in every danger; the pessimist sees danger in every opportunity.",
    "A positive attitude may not solve all your problems, but it will annoy enough people to make it worth the effort.",
    "There are no menial jobs, only menial attitudes.",
    "hard work beats talent when talent" ,
    "if you do what you've always ",
    "You can tell what a man is by what he does when he hasn’t anything to do.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
    "On the mountains of truth you can never climb in vain: either you will reach a point higher up today, or you will be training your powers so that you will be able to climb higher tomorrow." ,
    "People of mediocre ability sometimes achieve outstanding success because they don't know when to quit. Most men succeed because they are determined to.",
    "Success seems to be connected with action. Successful men keep moving. They make mistakes, but they don't quit.",
    "Good ideas are not adopted automatically. They must be driven into practice with courageous patience." ,
    "In order to get from what was to what will be, you must go through what is.",
    "Perseverance is not a long race; it is many short races one after another.",
    "Victory is always possible for the person who refuses to stop fighting.",
    "Learning is not compulsory. . . neither is survival.",
    "What we think or what we believe is, in the end, of little consequence. The only thing of consequence is what we do.",
    "Have no fear of perfection you'll never reach it.",
    "The important thing is this: to be able, at any moment, to sacrifice what we are for what we could become.",
    "Getting what you want is not nearly as important as giving what you have.To gain that which is worth having, it may be necessary to lose everything else.",
    "Sweat plus sacrifice equals success.",
    "One half of knowing what you want is knowing what you must give up before you get it.",
    "Dreams do come true, if we only wish hard enough, You can have anything in life if you will sacrifice everything else for it.",
    "Artists must be sacrificed to their art. Like bees, they must put their lives into the sting they give.",
    "Success is often the result of taking a misstep in the right direction.",
    "A successful man is one who can lay a firm foundation with the bricks others have thrown at him.",
    "Are you bored with life? Then throw yourself into some work you believe in with all your heart, live for it, die for it, and you will find happiness that you had thought could never be yours.",
    "Instead of worrying about what people say of you, why not spend time trying to accomplish something they will admire.",
    "The successful man will profit from his mistakes and try again in a different way.",
    "Inaction breeds doubt and fear. Action breeds confidence and courage. If you want to conquer fear, do not sit home and think about it. Go out and get busy.",
    "Success means getting up one more time than you fall.",
    "Never stop. Living well is the best revenge.",
    "Think like a man of action, act like a man of thought.",
    "The difference between what we do and what we are capable of doing would suffice to solve most of the world’s problem.",
    "An ounce of practice is worth more than tons of preaching.",
    "First they ignore you, then they laugh at you, then they fight you, then you win.",
    "I look only to the good qualities of men. Not being faultless myself, I won’t presume to probe into the faults of others.",
    "Man becomes great exactly in the degree in which he works for the welfare of his fellow",
    "I suppose leadership at one time meant muscles; but today it means getting along with people.",
    "Constant development is the law of life, and a man who always tries to maintain his dogmas in order to appear consistent drives himself into a false position",
    "don’t let yesterday take up too much of today",
    "you learn more from failure than from success don’t let it stop you. failure builds character",
    "it’s not whether you get knocked down, it’s whether you get up",
    "if you are working on something that you really care about, you don’t have to be pushed. the vision pulls you",
    "we may encounter many defeats but we must not be defeated",
    "we generate fears while we sit. we overcome them by action",
    "security is mostly a superstition. life is either a daring adventure or nothing",
    "the man who has confidence in himself gains the confidence of others",
    "the only limit to our realization of tomorrow will be our doubts of today",
    "creativity is intelligence having fun",
    "what you lack in talent can be made up with desire, hustle and giving 110% all the time",
    "to see what is right and not do it is a lack of courage",
    "today’s accomplishments were yesterday’s impossibilities",
    "the only way to do great work is to love what you do. if you haven’t found it yet, keep looking. don’t settle",
    "you don’t have to be great to start, but you have to start to be great",
    "leaders never use the word failure. they look upon setbacks as learning experiences"]


    goodquote = False

    while not goodquote:
        model = {}

        generated_quotes = []

        dataset_file = None

        quotes = ""

        # -------------------------------------------------------




        dataset_file = QUOTES



        for line in dataset_file:

            line = line.lower().split()
            for i, word in enumerate(line):

                if i == len(line) - 1:
                    model['END'] = model.get('END', []) + [word]
                else:
                    if i == 0:
                        model['START'] = model.get('START', []) + [word]
                    model[word] = model.get(word, []) + [line[i + 1]]
        # ----------------------------------------------------------------------

        while True:

            if not generated_quotes:
                word = model['START']

            elif generated_quotes[-1] in model["END"]:
                break

            else:
                word = model[generated_quotes[-1]]
            generated_quotes.append(random.choice(word))

        verb = False
        for x in generated_quotes:
            if x in verbs:
                verb = True
            quotes += x
            quotes += " "

        if len(quotes)>=12 and len(quotes)<=130 and verb:
            goodquote = True

        if quotes[len(quotes)-2]=="o" and quotes[len(quotes)-3]=="t":
            ends = ["succeed","win","be powerful","not be afraid"]
            add = random.randint(0, len(ends)-1)
            quotes += ends[add]



    Pass = True
    addposwords = []
    finalquotes = []
    lastline = ""
    same = 0
    for line in QUOTES:
        line = line.lower().split()
        if same >= 1:
            add = ""
            for q in lastline:
                add += q
                add += " "
                addposwords.append(add)
            add+="-"
            finalquotes.append(add)
        same = 0
        for element in line:

            lastline = line
            for w in generated_quotes:

                if w == element:
                    for i in addposwords:
                        if i==w:
                            Pass = False
                    if Pass==True:
                        same += 1
            Pass=True



    q = Question.objects.create(Quote_text=quotes, pub_date=timezone.now(),posquote = finalquotes)
    latest_question_list = Question.objects.order_by('-pub_date')[:1]

    template = loader.get_template('polls/Generate_Quotes.html')

    context ={
        'quote': q,
        'latest_question_list': latest_question_list,

              }
    return HttpResponse(template.render(context, request))


def info(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)

        last = ""
        f = []
        delete=False
        x = 0

        for i in question.posquote:
            if not i=="-" and delete==False and i!="[" and i!=",":
                last += i

            if i=="-" and x==0 :
                delete = True

            if delete==True:
                x+=1
                if x==2:
                    x=0
                    delete=False

            if i=="-":
                last+="'"
                f.append(last)
                last = ""


    except Question.DoesNotExist:
        raise Http404("Quote does not exist")
    return render(request, 'polls/info.html', {'quote': question,"posquotelist":f})


def add(request,question_id):
    all = BEST.objects.all()
    x = Question.objects.get(pk=question_id)
    y = x.Quote_text
    inbest = False

    for i in all:
        if i.best == x.Quote_text:
            inbest = True

    if not inbest:
        q = BEST(best=y)
        q.save()

    allbestlist = BEST.objects.order_by('-id')
    template = loader.get_template('polls/Best_Quotes.html')
    context = {
        'allbestlist': allbestlist,

    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def bobr(request):

    template = loader.get_template('polls/bobrvaders.html')
    if request.POST.get('klic', '') == 'brbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrAbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrAbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrAbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrAbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrAbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrAbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrAbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrAbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrAA':
        context = {"heslo": "aFLRX404XRLF"}
    else:
        context = {"heslo": "Gratuluji, nějak se ti podařilo hacknout tuhle hru. Ale heslo na školní Wi-Fi ti dám stejně až potom, co dohraješ BobrVaiders ;-)"}
    return HttpResponse(template.render(context, request))



