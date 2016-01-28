init:
    $ end_text_rfe = "IIchan Eroge Team\nи Lilly On The Bible\nблагодарят вас за время, уделённое игре и моду!\n\nБлагодарности:\n\nPyTom'у за движок Ren'Py.\n\nСергею «SilentOwl» Ейбогу\nза предоставленный саундтрек.\n\nГруппе «Nobody.One» за\nпредоставленый саундтрек к моду.\n\nОлеже Двачевскому и Алексею «Mio Akiyama»\nза помощь с кодом мода.\n\nОгромное спасибо Семёну «Мику» за помощь с Двачевской и поиском фонов.\n\nСпасибо Александру «PRO100_Sasha» за помощь с вычиткой.\n\nСайту freesounds.org\nза бесплатные звуки.\n\nСайтам iichan.hk и 2ch.hk.\n\nВсем, кто помогал работать над модом (ilyamodder, H8R и другие)\n\nВсем, кто поддерживал нас, ждал и верил!\n\nАвторы мода:\n\nBivnjatkO - сценарий.\n\ntlsd (Lilly On The Bible) - код, фоны, звуки, вычитка, отсебятина.\n\n\n\n\n\n\n\nКОНЕЦ.\n"

init 2:
    $ pav = Character(u'Павел', color="#993333", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")
    $ mav = Character(u'Мать', color="#99CCFF", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")
    $ bab = Character(u'Зоя Фёдоровна', color="#3366CC", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")
    $ lis = Character(u'Лысый', color="#FFFF66", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")
    $ yar = Character(u'Ярик', color="#FF0033", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")
    $ bat = Character(u'Игнат Борисович', color="#06DCFB", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")
    $ pim = Character(u'Пионер Маньяк', color="#FF2626", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")
    $ prap = Character(u'Прапор', color="#40FF00", what_color="E2C778", drop_shadow = [ (-1, -1), (1, -1), (-1, 1), (1, 1) ], drop_shadow_color = "#000")
    image bg gym = "rfe/bg/gym.jpg"
    image bg gym2 = "rfe/bg/gym2.jpg"
    image bg gym3 = "rfe/bg/gym3.jpg"
    image bg kitchenrfe = "rfe/bg/kitchen.jpg"
    image bg parad = "rfe/bg/paradnaya.jpg"
    image bg alisahru = "rfe/bg/int_alisa_hru.jpg"
    image bg babkaroom = "rfe/bg/babkaroom.jpg"
    image bg baseya = "rfe/bg/basementya.jpg"
    image bg batkokitchen = "rfe/bg/batkokitchen.jpg"
    image bg batkohouse = "rfe/bg/batkohouse.jpg"
    image bg kepepe = "rfe/bg/kepepe.jpg"
    image bg kladbiwe = "rfe/bg/kladbiwe.jpg"
    image bg sigroad = "rfe/bg/higroad.jpg"
    image dv smile coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_4_body.png",(0,0), "rfe/sprites/dv_4_coat.png",(0,0), "images/1080/sprites/normal/dv/dv_4_smile.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv normal coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_4_body.png",(0,0), "rfe/sprites/dv_4_coat.png",(0,0), "images/1080/sprites/normal/dv/dv_4_normal.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv surprise coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_1_body.png",(0,0), "rfe/sprites/dv_1_coat.png",(0,0), "images/1080/sprites/normal/dv/dv_1_surprise.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv scared coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_1_body.png",(0,0), "rfe/sprites/dv_1_coattie.png",(0,0), "images/1080/sprites/normal/dv/dv_1_scared.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv shy coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_3_body.png",(0,0), "rfe/sprites/dv_3_coattie.png",(0,0), "images/1080/sprites/normal/dv/dv_3_shy.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv sad coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_3_body.png",(0,0), "rfe/sprites/dv_3_coattie.png",(0,0), "images/1080/sprites/normal/dv/dv_3_sad.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv guilty coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_3_body.png",(0,0), "rfe/sprites/dv_3_coattie.png",(0,0), "images/1080/sprites/normal/dv/dv_3_guilty.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv angry coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_5_body.png",(0,0), "rfe/sprites/dv_5_coattie.png",(0,0), "images/1080/sprites/normal/dv/dv_5_angry.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv cry coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_1_body.png",(0,0), "rfe/sprites/dv_1_coattie.png",(0,0), "images/1080/sprites/normal/dv/dv_1_cry.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv laugh coattie = im.MatrixColor( im.Composite((900,1080), (0,0), "images/1080/sprites/normal/dv/dv_4_body.png",(0,0), "rfe/sprites/dv_4_coattie.png",(0,0), "images/1080/sprites/normal/dv/dv_4_laugh.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv laugh coattie close = im.MatrixColor( im.Composite((1050,1080), (0,0), "images/1080/sprites/close/dv/dv_4_body.png",(0,0), "rfe/sprites/dv_4_coattie_close.png",(0,0), "images/1080/sprites/close/dv/dv_4_laugh.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv smile coattie close = im.MatrixColor( im.Composite((1050,1080), (0,0), "images/1080/sprites/close/dv/dv_4_body.png",(0,0), "rfe/sprites/dv_4_coattie_close.png",(0,0), "images/1080/sprites/close/dv/dv_4_smile.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image dv surprise coattie close = im.MatrixColor( im.Composite((1050,1080), (0,0), "images/1080/sprites/close/dv/dv_1_body.png",(0,0), "rfe/sprites/dv_1_coattie_close.png",(0,0), "images/1080/sprites/close/dv/dv_1_surprise.png"), im.matrix.tint(0.83, 0.88, 0.92) )