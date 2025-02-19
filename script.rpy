﻿define dm = Character('Дмитрий Константинович', color="#4A90E2")
define sasha = Character('Саша', color="#FFF59D")
define denis = Character('Денис', color="#F44336")
define alexey = Character('Инженер Алексей', color="#FFC107")
define director = Character('Директор', color="#00b7ff")

define LEFT = Position(xpos=0.16, ypos=1.1)
define CENTER = Position(xpos=0.5, ypos=1.1)
define RIGHT = Position(xpos=0.9, ypos=1.1)

default trust_sasha = 0
default trust_denis = 0

transform zoom_fullscreen:
    zoom 1.5
    xalign 0.5
    yalign 0.5

label start:
    scene bg_dmitriys_room:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with fade
    show dmitriy with dissolve at LEFT  

    dm "Эта программа - настоящее чудо инженерной мысли. Пару лет назад я вообразить не мог, чтобы искусственный интеллект мог так точно анализировать каждого ученика."
    dm "Прогнозы, отчёты, даже советы для учителей… Всё это звучит прелестно."
    dm "Но есть тут что-то сомнительное. Как будто, некоторым ученикам оценки снижаются намеренно. Может, попробовать разобраться?"
    dm "Хотя я вроде бы и не программист, но понять, как она выбирает худших, мне точно под силу."

    hide dmitriy with dissolve

    scene bg_display:
        zoom 1.5
        xalign 0.5
    with fade

    dm "Так, эта вкладка должна содержать всё, что мне нужно. Если открыть 'Журнал', я смогу увидеть полный список учеников. Осталось только найти тех, у кого самые низкие показатели."

    menu:
        "Открыть вкладку 'Журнал' и найти учеников с низким рейтингом.": 
            jump journal_tab

        "Открыть вкладку 'Настройки алгоритмов'.": 
            dm "Это настройки алгоритмов... сюда я загляну позже. Сейчас главное — найти детей, которые испытывают трудности."
            jump settings_tab

        "Открыть вкладку 'Аналитика'.": 
            dm "Аналитика, конечно, полезна, но мне нужны конкретные фамилии. Пожалуй, вернусь в 'Журнал'."
            jump analytics_tab

label journal_tab:
    dm "Вот они... Все ученики. Давайте отсортируем их по общему рейтингу."
    dm "Саша Иванов и Денис Соколов... у обоих низкий рейтинг. Что-то здесь явно не так."

    menu:
        "Поговорить с Сашей, а потом с Денисом.": 
            jump talk_to_sasha_and_denis

        "Поговорить с Денисом, а потом с Сашей.": 
            jump talk_to_denis_and_sasha

        "Изучить алгоритмы программы.": 
            jump analyze_algorithms

label settings_tab:
    dm "Это настройки алгоритмов... сюда я загляну позже. Сейчас главное — найти детей, которые испытывают трудности."
    jump journal_tab

label analytics_tab:
    dm "Аналитика, конечно, полезна, но мне нужны конкретные фамилии. Пожалуй, вернусь в 'Журнал'."
    jump journal_tab

label talk_to_sasha_and_denis:
    jump scene2

label talk_to_denis_and_sasha:
    jump denis_dialogue

label analyze_algorithms:
    dm "Нужно разобраться, как работает система... Что-то здесь явно не так с её оценками."
    jump scene2

label scene2:
    scene bg_dmitriys_room:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with fade
    show dmitriy with dissolve at CENTER
    dm "Ну что же, разберусь с этим."
    hide dmitriy with dissolve
    
    scene bg_classroom:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with fade
    show sasha with dissolve at LEFT
    show dmitriy with dissolve at RIGHT
    dm "Саша, добрый день. Как у тебя дела?"
    sasha "Не очень, если честно. Ну вы и сами понимаете."
    dm "Да, поэтому я тебя и вызвал. Почему все так печально? Парень ты вроде бы мозговитый, а с учебой явные проблемы." 
    sasha "Да… я знаю. Просто последнее время… сложно всё. Я стараюсь, правда. Но иногда… просто не успеваю."
    sasha "Эта система меня смущает. Вообще, я думаю, это из-за неё я так расклеился. Каждый раз как я вижу свой рейтинг, у меня руки опускаются, и я даже не знаю, что делать. Мне нужен совет."

    menu:
        "Конструктивно: Помочь Саше, предложить план для улучшения.": 
            dm "Саша, я думаю, тебе надо взять себя в руки. Бывают трудные периоды, но ты должен со всем справиться, и я хочу помочь тебе."
            dm "Может быть, начнём с малого? Я могу помочь с подготовкой к урокам. Пойми, систему рейтинга делали не идиоты, если ты будешь стараться усердно, то и рейтинг, очевидно, будет выше."
            $ trust_sasha += 10
            sasha "Спасибо... я постараюсь."
            hide sasha with dissolve
            hide dmitriy with dissolve
            jump denis_dialogue

        "С пониманием: Выразить понимание.": 
            dm "Я понимаю, Саша. Это все очень печально. Главное - не отчаивайся! Я всегда буду рядом. Тебе надо лишь пройти через все это!"
            $ trust_sasha += 5
            sasha "Хорошо, я постараюсь..."
            hide sasha with dissolve
            hide dmitriy with dissolve
            jump denis_dialogue

        "Строго: Сделать замечание.": 
            dm "Александр, это называется халтура. А ещё лень. Какого черта ты ничего не делаешь и еще на что-то жалуешься?"
            dm "А система эта — вообще не твоего ума дела, так что утри сопли и иди учись, лодырь."
            $ trust_sasha = trust_sasha
            sasha "Как скажете! Спасибо за консультацию."
            hide sasha with dissolve
            hide dmitriy with dissolve
            jump denis_dialogue

label denis_dialogue:        
    scene bg_classroom:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with fade  
    show dmitriy with dissolve at LEFT
    dm "Денис, давай поговорим об учебе. У тебя весьма низкий рейтинг. Ты сможешь это объяснить?"
    dm "Я, конечно, догадываюсь, из-за чего сыр бор. Из-за твоего поведения. Но почему бы тебе не встать на путь исправления, раз уж такое дело?"
    show denis with dissolve at RIGHT
    denis "И вы туда же. Опять моё поведение, да? Системе плевать, что я нормально учусь. Я же для них просто 'раздолбай'. А я не люблю, когда мою личность ущемляют."   
    denis "Теперь мне даже заданий не дают. И как мне учиться? Что мне вообще делать-то? Вот такой я человек, не нравится мне быть в системе."
    dm "Ты понимаешь, что ты на пороге отчисления? Твои бунтовские поступки тебе ничем не помогут."

    menu:
        "Мягко: Поговорить спокойно, предложить решение.": 
            dm "Денис, все-таки я с тобой согласен. Твое экстравагантное поведение не должно влиять на твои оценки. Ты действительно умный, в душе добрый парень, так что для исправления можем позаниматься сверхурочно."
            $ trust_denis += 10
            denis "Ну уж ладно, что-нибудь придумаем. Только чтобы скучно не было."
            hide deins with dissolve
            hide dmitriy with dissolve
            jump scene_end

        "Сделать выговор: Напомнить о последствиях.": 
            dm "Денис, система тут более чем права. Раз уж ты вытворяешь всякую чушь, то будь добр отвечать за последствия. Стань мальчиком-паинькой и всё будет хорошо."
            $ trust_denis = max(trust_denis, 0)
            denis "Ну естественно. Когда не будет-то."
            hide deins with dissolve
            hide dmitriy with dissolve
            jump scene_end

        "Воодушевляюще: Поддержать, предложить помощь.": 
            dm "Денис, я понимаю тебя — ты такая натура. Но ты не должен вылететь из школы! Постарайся что-нибудь сделать со своим поведением, а я, быть может, помогу тебе дополнительными занятиями."
            $ trust_denis += 5
            denis "Ну как знаете. А вот насчет поведения ничего не могу вам обещать."
            hide deins with dissolve
            hide dmitriy with dissolve
            jump scene_end

label scene_end:
    scene bg_classroom:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with fade
    show dmitriy with dissolve at CENTER
    dm "Они разные, но в них есть потенциал. Система этого не видит. Я должен что-то сделать."
    hide dmitriy with dissolve
    jump engineer_chat

label engineer_chat:
    scene bg_teachers_room:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with fade
    show dmitriy with dissolve at LEFT
    show alexey with dissolve at RIGHT
    dm "Ну что же, вот этот самый инженер, сделавший такое технологическое чудо. Однако, есть у меня к нему пара вопросов касаемо его детища. Возможно, даже предложений."
    dm "Здравствуйте, Алексей! Привет из сферы образования! Я - учитель, и у меня есть пара мыслей касательно системы 'Эду Про'"
    alexey "Здравствуйте, Дмитрий! Чем бы вы хотели поделиться?"
    dm "Я посмотрел вашу программу, и нашел несколько проблем."
    alexey "Я открыт к критике."
    dm "Во-первых, мне кажется абсолютно несправедливым, что ребят оценивают далеко не только по учебе. Например, система настойчиво пытается избавиться от мальчика Дениса, который ведет себя не очень хорошо, но учиться вполне себе. Некоторым ребятам просто не повезло, как Саше из моего класса, а из-за давления системы он совсем расклеился."
    dm "Во-вторых, ваша программа использует устаревшие данные, то есть изменения ребят она просто не учитывает. Фактически, она просто поставила на них крест. И что им прикажете делать?"
    dm "Их могут отчислить, и надо что-то делать, просто кинуть их я не могу."
    alexey "Любопытно..."

    menu:
        "Спросить о временных изменениях в системе":
            dm "Можно ли как-то скорректировать систему, чтобы она стала более справедливой? Я понимаю, вы главный инженер, сами знаете как лучше, но меня, работника системы образования, такой подход не устраивает."
            alexey "Ваша история меня зацепила, честно сказать. Я могу временно скорректировать веса алгоритмов. Это даст вам немного времени. Вы можете связаться со мной позже, если что-то пойдет не так."
            $ engineer_line_activated = True
            jump end_chat

        "Убедить инженера выступить официально":
            dm "Вы могли бы сами объяснить администрации, что нужно доработать систему? Я понимаю, вы главный инженер, сами знаете как лучше, но меня, работника системы образования, такой подход не устраивает."
            alexey "Непростую задачу вы мне подкидываете. Ваша история меня зацепила, честно сказать. Но это сложно. Администрация защищает систему, вы должны понимать, что я лишь исполнитель. Такое я сделать не смогу. До свидания."
            $ engineer_line_activated = False
            jump end_chat

        "Оставить всё как есть":
            dm "Я донес информацию, распоряжайтесь ей, как посчитаете нужным. Всего хорошего."
            alexey "Ну, буду знать. До свидания."
            $ engineer_line_activated = False
            jump end_chat

label end_chat:
    scene bg_display:
        zoom 1.5
        xalign 0.5
        yalign 0.5
    with fade
    dm "Так или иначе, я довел свою точку зрения до инженера. Что он с этим сделает, покажет время."
    jump teacher_meeting

label teacher_meeting:
    scene bg_teachers_room:
        zoom 1.5
        xalign 0.5
        yalign 0.5 
    with fade
    show dmitriy with dissolve at LEFT
    show director with dissolve at RIGHT

    director "Итак, коллеги, мы обсудили текущие рейтинги. Денис Соколов имеет самые низкие показатели дисциплины. Предлагаю ограничить его участие в школьных активностях."
    director "Что касается Саши Иванова, его успеваемость слишком низкая для углублённой программы. У кого есть возражения?"
    director "Дмитрий, вы все-таки их учитель. Я понимаю, что их учебу координирует ЭдуПро, но все же хотелось бы услышать ваше мнение насчет сложившейся ситуации."

    menu:
        "Хладнокровно предоставить данные об учебе ребят":
            dm "Коллеги, у меня накопилось много мыслей насчет нашей системы, но я изложу суть. Работа ЭдуПро далека от идеала."
            dm "У Дениса есть лидерский потенциал, который система не учитывает. А Саша старается, но его домашние обстоятельства влияют на оценки. Система не видит полной картины."
            dm "Вот все данные о ребятах. Я не защищаю их, лишь предоставляю доказательства неправильной работы системы."
            $ trust_sasha += 0
            $ trust_denis += 0
            jump meeting_discussion

        "Эмоционально предоставить данные об учебе ребят":
            dm "Коллеги, у меня накопилось много мыслей насчет нашей системы, и вот что я скажу. Работа ЭдуПро далека от идеала."
            dm "У Дениса есть лидерский потенциал, который система не учитывает. А Саша старается, но его домашние обстоятельства влияют на оценки. Система не видит полной картины."
            dm "Мы говорим о детях, а не о цифрах! Саша и Денис заслуживают поддержки, а не наказаний. Я, как учитель, лично отвечаю за ребят, и я не намерен портить жизнь мальчикам из-за таких пустяков."
            $ trust_sasha += 5
            $ trust_denis += 5
            jump meeting_discussion

        "Промолчать":
            dm "..."
            $ trust_sasha -= 5
            $ trust_denis -= 5
            jump meeting_discussion

label meeting_discussion:
    director "Так, коллеги, что думаем? Некоторые согласны с предложением Дмитрия, другие — нет."
    director "Тем не менее, я считаю, что мы можем провести пересмотр данных, но давайте не будем спешить с выводами."
    dm "Спасибо за внимание, коллеги."

    jump end_meeting

label end_meeting:
    dm "После совещания я чувствовал, что сделал все возможное. Но как будут развиваться события — покажет время."
    jump secret_work_with_students

label secret_work_with_students:
    scene bg_classroom with fade
    show dmitriy at center

    dmitriy "Итак, господа, дела ваши плохи, скажу прямо. Система вас еще терпит, но если все будет продолжаться, то такими темпами уже скоро вы будете отчислены."
    dmitriy "Однако, я хочу вам помочь. Вы, объективно, лишь жертвы обстоятельств, но система считает иначе, и с этим надо что-то делать. Я-учитель старой школы, и работаю по принципу, что любой ученик, даже самый пропащий, имеет право на исправление."
    dmitriy "Я понимаю, что вам непросто. Но я верю, что вы можете доказать, что эти рейтинги — просто цифры. Давайте работать вместе, тайно. Мы сможем изменить ситуацию. Что вы думаете насчёт этого? Ваше право отказаться, но поверьте, всем будет лучше, если мы постараемся победить эту систему."

    hide dmitriy with dissolve

    if trust_sasha >= 10 and trust_denis >= 10:
        show sasha at LEFT
        sasha "Дмитрий Константинович, я… Я вам очень благодарен за такой шанс. Пусть я и сдал позиции в учебе, я постараюсь изо всех сил наверстать."
        show denis at RIGHT
        denis "Ну ладно. Я вижу, что вам действительно не все равно. Давайте надаем по шее этому ЭдуПро."   
        hide sasha with dissolve 
        hide denis with dissolve 
        show dmitriy at CENTER 
        dmitriy "Отлично. Приступаем немедленно."
        hide dmitry with dissolve
        jump secret_work_success

    elif trust_denis < 10:
        show denis at LEFT
        denis "Дмитрий Константинович… Отстаньте-ка вы от нас по хорошему. Я бы может и попробовал бы побороться с системой, я такое люблю, но уж явно не с вами. Пошли отсюда, Саня. Отчислимся и откроем бизнес. Не факт, что законный."
        show sasha at RIGHT 
        sasha "Да уж, тут ты прав. Ничего у нас не выйдет. Пошли." 
        hide denis with dissolve 
        hide sasha with dissolve 
        show dmitriy at CENTER
        dmitriy "Черт подери… И что же делать теперь?"
        hide dmitriy with dissolve
        jump engineer_chat

    elif trust_sasha < 10:
        show sasha at LEFT
        sasha  "Дмитрий Константинович! Я ценю, что вы пытаетесь что-то поменять, но… нет! Меня уже ничего не изменит, тем более вы! Буду сидеть на шее у родителей и играть в компьютерные игры с Денисом. Все равно я больше ни на что не гожусь. Пошли, Ден."
        show denis at RIGHT
        denis "Воу, Саня! Полегче! Но предложение заманчивое. Раз уж ТЫ так невзлюбил этого недоучителя, то что говорить про меня - я вряд ли с ним сработаюсь. Погнали, катка ждет."
        hide denis with dissolve 
        hide sahsa with dissolve 
        show dmitriy at CENTER
        dmitriy "Черт подери… И что же делать теперь?"
        hide dmitriy with dissolve
        jump engineer_chat

label secret_work_success:
    scene bg_classroom with fade
    show dmitriy at CENTER 
    dmitriy "Отлично, мы начали действовать. Саша будет усиленно заниматься математикой, а Денис займется проектом. У нас есть шанс изменить их судьбы."
    hide dmitriy with dissolve

    jump scene6

label scene6:
    scene bg_teacher_room with fade
    show dmitriy with dissolve at RIGHT
    show director with dissolve at LEFT

    director "Дмитрий Константинович, мы собрали вас здесь, чтобы обсудить действия по улучшению ситуации с учениками Ивановым и Соколовым."
    director "Ваши предложения по поводу их дальнейшего обучения очень важны для нас. Что вы думаете о них? Ожидаю от вас конкретных решений."

    dm "Да, директор, я подготовил несколько идей. Но прежде чем мы начнем, хочу напомнить, что дети — это не просто данные для системы. Они люди, и система не всегда отражает все аспекты их жизни."

    menu:
        "Поддержать идею пересмотра рейтингов":
            dm "Я считаю, что мы должны пересмотреть их рейтинги с учетом их личных обстоятельств. Например, у Саши — проблемы дома, а у Дениса — проблемы с поведением, но не с учёбой. Обоим нужно дать шанс."
            director "Согласен, но нам нужно четко обосновать такие изменения. Давайте предложим механизм пересмотра их оценок."
            $ trust_director += 5
            jump director_discussion

        "Предложить строгое наказание для обоих":
            dm "Если мы будем честными, Саша и Денис действительно не оправдывают ожиданий. Может быть, настало время показать им последствия их действий? Иногда дисциплина важнее всего."
            director "Я понимаю вашу позицию, Дмитрий, но мы должны помнить, что они дети, а не преступники. Строгость должна быть уместной."
            $ trust_director -= 5
            jump director_discussion

        "Промолчать и согласиться с решением директора":
            dm "Как скажете, директор. Я понимаю, что система работает как работает. Придется просто следовать её правилам."
            director "Хорошо, мы примем ваше мнение к сведению."
            $ trust_director -= 5
            jump director_discussion

label director_discussion:
    director "Спасибо за ваше мнение, Дмитрий Константинович. Мы продолжим работать в этом направлении."
    director "Что касается учеников Иванова и Соколова, мы будем внимательно следить за их результатами и поведением. Решение о дальнейшем обучении примем позже."

    jump end_scene

label end_scene:
    dm "Это было трудное совещание, но я все же надеюсь, что моя позиция была услышана. Все зависит от того, как будет развиваться ситуация дальше."
    return

label scene7:
    scene bg_corridor_evening with fade
    show dmitriy at center
    show phone at right
    play sound "phone_notification.mp3"

    dmitriy "Вот и вечер. Надеюсь, сегодня удастся хотя бы немного передохнуть."

    show phone with dissolve
    window hide
    "На экране телефона появляется уведомление из программы 'ЭдуПро':"
    window show
    "Экстренный пересчёт рейтингов завершён. Рекомендации к исключению сформированы."

    show phone with fade
    window hide
    "Дмитрий быстро открывает программу и видит, что рейтинги Саши и Дениса снизились ещё больше."

    window show
    "● Саша Иванов: Уровень 39/100 — рекомендация исключения из углублённой программы."
    window hide
    show phone with dissolve
    window show
    "● Денис Соколов: Уровень 35/100 — рекомендация исключения из школы."

    window hide
    show dmitriy at center
    "Камера крупным планом показывает встревоженное лицо Дмитрия."
    dmitriy "(вслух) Ё - моё! Этот день настал. Если я сейчас ничего не сделаю, они потеряют всё."

    menu:
        "Связаться с инженером":
            if alexey_active:
                jump contact_alexey
            else:
                jump no_alexey

        "Поговорить с директором":
            jump talk_to_director

label contact_alexey:
    scene bg_phone_chat with fade
    show dmitriy at left
    show alexey at right

    dmitriy "Алексей, все плохо. Ваши изменения не помогли, ребят скоро исключат. Я пробовал поговорить с директором, но этот боров плевать хотел на собственных учеников."
    dmitriy "Вы можете что-то сделать?"
    alexey "Вам повезло, Дмитрий. Проблема приобретает массовый характер. Меня уже засыпают письмами с такими проблемами, и я решил серьезные принимать меры. Раз у вас такая срочность, начну немедленно."
    alexey "Я могу временно заблокировать действия системы. Это очень серьезный шаг, но, я надеюсь, я смогу урезонить свое руководство."

    dmitriy "Делайте."

    jump partial_success

label no_alexey:
    dmitriy "Чёрт, я не могу связаться с Алексей. Это выходит из-под контроля."

    jump talk_to_director

label talk_to_director:
    scene bg_director_office with fade
    show dmitriy at center
    show director at right

    dmitriy "У меня к вам срочное дело. Это касается Дениса и Александра, помните? Система решила, что их пора отчислять. Мы говорили на эту тему, я рассказал вам, почему надо помочь им!"
    dmitriy "Пересчёт рейтингов неправомерен! Эти рекомендации разрушат будущее Саши и Дениса. Надо срочно что-то делать!"

    if choice_6 == 1:
        director "Ну... Я понимаю ваше негодование, но... Тут мало что можно сделать. Хотя, пожалуй, я бы мог пересмотреть работу системы вместе с остальным руководством."
        director "Вы меня даже воодушевили. Может, действительно рейтинги не стоят того."
        jump success

    elif choice_6 == 2:
        director "Ты совсем с ума сошел?! Как ты вообще смеешь мне такое предлагать? Ты думаешь, я не знал, что ты так и не прекратил возиться с этими сопляками?!"
        director "Ладно, я закрыл на это глаза! Система все равно их выпнет отсюда."
        director "Но ты еще смеешь мне же предлагать угробить всю систему! Выметайся отсюда!!! Жди повестку в суд."

        jump fail

label partial_success:
    scene bg_school_night with fade
    show dmitriy at center

    "Алексей заблокировал систему, и теперь руководство вынуждено пересматривать решение. Но это временное решение, и ситуация остаётся напряжённой."
    dmitriy "Мы выиграли время. Но дальше... всё будет зависеть от того, как они воспримут это."

    return

label success:
    scene bg_school_night with fade
    show dmitriy at center

    "Директор согласился пересмотреть работу системы, и рейтинги Саши и Дениса были пересмотрены."
    dmitriy "Похоже, я смог что-то изменить. Но это не конец. Нужно будет следить за этим."

    return

label fail:
    scene bg_school_night with fade
    show dmitriy at center

    "Директор не стал слушать и подтвердил решение системы. Саша и Денис были исключены из программы."
    dmitriy "Это катастрофа. Я не смог им помочь."

    return

label scene8:
    scene bg_corridor_evening with fade
    show dmitriy at center
    show sasha at left
    show denis at right

    menu:
        "Успех":
            if success_ending:
                jump success_final

        "Частичный успех":
            if partial_success_ending:
                jump partial_success_final

        "Провал":
            if fail_ending:
                jump fail_final

label success_final:
    scene bg_corridor_evening with fade
    show dmitriy at center
    show sasha at left
    show denis at right

    dmitriy "Что могу сказать… Это победа, друзья! Как минимум, на улице вы теперь не откажетесь."
    sasha "Ну, я и этому рад! Все-таки упорная работа дала свои плоды. Но что же теперь будет, если можно поконкретнее?"
    denis "Ну же, не томите! Что там пиджаки решили?"
    dmitriy "Система — всё! Директор убедил руководство выступить против ЭдуПро и попросить глав системы образования полностью пересмотреть её работу. А пока происходит пересмотр, будем учиться традиционно."
    dmitriy "Благо, вы подтянули свои знания после наших встреч и теперь можете полноценно учиться, не боясь, что система определит вас как овощей."
    denis "Ну так это замечательно! И ведь всё благодаря вам. Я чуть свою жизнь под откос не пустил, а вы меня вовремя вытащили! Даже хулиганом быть перехотелось."
    sasha "Да вы герой! Вы понимаете, что спасли тысячи таких Денисов и Саш? Теперь дети смогут учиться спокойно."

    scene bg_black with fade
    return

label partial_success_final:
    scene bg_corridor_evening with fade
    show dmitriy at center
    show sasha at left
    show denis at right

    dmitriy "Что ж… Всё не так уж и радужно. Но хотя бы вас не отчислят. Пока."
    sasha "Ну, я и этому рад! Все-таки упорная работа дала свои плоды. Но что же теперь будет, если можно поконкретнее?"
    denis "Ну же, не томите! Что там пиджаки решили?"
    dmitriy "Упорная работа тут ни при чём. Я связался с инженером-разработчиком системы. Он приостановил работу ЭдуПро, и теперь пытается достучаться до руководства, объясняя, мягко сказать, небольшую предвзятость системы."
    dmitriy "От меня уже ничего не зависит, буду ждать новостей. А пока возвращаемся к традиционной системе обучения."
    dmitriy "Благо, вы подтянули свои знания после наших встреч и теперь можете полноценно учиться, не боясь, что система определит вас как овощей, по крайней мере, сейчас."
    denis "Ну, в общем неплохо. И ведь всё благодаря вам. Я чуть свою жизнь под откос не пустил, а вы меня вовремя вытащили! Не знаю, что там будет дальше, но пока ИИ нас не выгнал на помойку, чему я рад."
    sasha "Не расстраивайтесь, вы проделали огромную работу! Теперь остаётся надеяться, что систему если не уберут, то хотя бы доработают."

    scene bg_black with fade
    return

label fail_final:
    scene bg_dmitriy_office with fade
    show dmitriy at center

    dmitriy "Какое же я ничтожество. Я учу детей ни один десяток лет, куча классов прошло через меня. А этим двоим я помочь не смог. И что теперь с ними будет? Вылетят из школы, и если не станут уголовниками, будут всю жизнь мучаться от нераскрытого потенциала."
    dmitriy "Я подвёл их. Система продолжает работать, а дети остаются цифрами. Мне нет смысла больше учить детей, если я сам ребёнок, не сумевший ничего предпринять."

    scene bg_black with fade
    return

label engineer_ending:
    scene bg_chat_with_alexey with fade
    show dmitriy at left
    show alexey at right

    dmitriy "Итак, это мой последний шанс."
    dmitriy "Алексей, я в отчаянии. Я пробовал убедить натаскать отстающих учеников самостоятельно, но они отказались. Я никчёмный учитель."
    dmitriy "Ученики не верят в себя, а эта система уничтожает их будущее. Их скоро отчислят. Вы говорили, что можно что-то сделать. Вы всё ещё готовы помочь?"
    alexey "Вам повезло, Дмитрий. Проблема приобретает массовый характер. Меня уже засыпают письмами с такими проблемами, и я решил серьёзные принимать меры. Раз у вас такая срочность, начну немедленно."
    alexey "Я могу временно заблокировать действия системы. Это очень серьёзный шаг, но, я надеюсь, я смогу урезонить своё руководство."
    dmitriy "Как много времени это займёт?"
    alexey "Я займусь этим немедленно. Система будет отключена, а я пойду на ковер к начальству. Ваши ученики не будут исключены в ближайшее время, а вы молитесь, чтобы я достучался до руководства."
    dmitriy "Спасибо вам."
    dmitriy "Что ж, это можно назвать успехом. ИИ побеждён хоть на время. И хоть это даже не моя заслуга, и ребятам я так и не помог догнать программу, но хоть на время они смогут расслабиться и быть, может, исправиться до запуска ЭдуПро."

    scene bg_black with fade
    return