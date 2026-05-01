"""
Lightweight stopword lists for the 24 official EU languages.

These are short, curated lists (50-150 words each) — enough to filter
high-frequency function words without overreaching into content terms.
No external dependencies, no downloads at runtime.

Sources: aggregated and trimmed from public-domain stopword corpora
(Stopwords-ISO, NLTK, spaCy defaults). Where multiple variants exist
we keep only the most common forms to stay compact.
"""
from __future__ import annotations

STOPWORDS: dict[str, frozenset[str]] = {
    "BG": frozenset("""
        а аз ако ала бе без беше би бил била били билo било близо
        бъдат бъде бяха в вас ваш ваша вече взема ви вие винаги все
        всеки всички всичко всяка във въпреки върху г ги главно го
        д да дали до докато докога дори досега доста е едва един
        ето за зад заедно заради защо защото и из или им има имат
        иска й каза как каква какво както какъв като кога когато
        което които кой който колко която къде където към ли м ме
        между мен ми мнго мога могат може мой моля момента му н на
        над назад най направи напред например нас не него нея ни
        ние никой нито но някои някой някоя няма обаче около освен
        особено от отгоре отново още пак по повече повечето под
        поне поради после почти прави пред преди през при пък
        първо с са сам само се сега си скоро след сме според сред
        срещу сте съм със също т тази така такива такъв там твой
        те тези ти то това тогава този той толкова том тук тъй
        тя тяхната тях у харесва ч че често чрез ще щом я
    """.split()),
    "CS": frozenset("""
        a aby ach aj ale ani aniž ano asi až bez bude budem budeš
        by byl byla byli bylo být co což cz či článek článku
        článkem během dál další den dnes do dva dvě ho i já jak
        jako je jeho jej její jeho jejich jen ještě jí jich jím
        jiné již jsem jsi jsme jsou jste k kam každý kde kdo když
        ke která které který kterou kterým ku mě mezi mi mně mnou
        mohou moje může na nad nám námi nás náš naše ne nebo neboť
        nebyl nelze není než nic nich ní nim nimi no o od ode okolo
        on ona oni ono ony pak pod podle pokud potom pouze pro
        proč proti přes přesto při proto protože před přede s se
        si sice skoro snad své svých svým svými ta tady tak také
        takže tam tato tě tedy téma ten tenhle tento ti to tobě
        toho tohle tomu tom tomto tu tuto ty tyto u už v vám vámi
        vás váš vaše ve více však všechno všichni vy vždy z za
        zde že
    """.split()),
    "DA": frozenset("""
        af alle andet andre at bare begge blev blive bliver da de
        dem den denne deres det dette dig din dine disse dit dog
        du efter eller en end er et fem fik fire flere folk for
        fra gennem god gør går har hav have hej hen hende hendes
        her hos hun hvad hvem hver hvilken hvis hvor hvordan hvorfor
        i ikke ind ingen intet ja jeg jer jeres jo kan kun kunne
        lad lidt lige man mand mange med meget men mens mere mig min
        mine mit må ned nej ni nogen noget nogle nu ny nær når og
        også op os otte over på sa se selv ser ses seks siden sig
        sige skal skulle som stor store syv sådan tag tage thi ti
        til tre to tre under var ved vi vil ville vor være været
    """.split()),
    "DE": frozenset("""
        ab aber alle allem allen aller alles als also am an ander
        andere anderem anderen anderer anderes anderm andern anders
        auch auf aus bei bin bis bist da damit dann der den des
        dem die das daß derselbe derselben denselben desselben
        demselben dieselbe dieselben dasselbe dazu dein deine deinem
        deinen deiner deines denn derer dessen dich dir du dies
        diese diesem diesen dieser dieses doch dort durch ein eine
        einem einen einer eines einig einige einigem einigen einiger
        einiges einmal er ihn ihm es etwas euer eure eurem euren
        eurer eures für gegen gewesen hab habe haben hat hatte
        hatten hier hin hinter ich mich mir ihr ihre ihrem ihren
        ihrer ihres euch im in indem ins ist jede jedem jeden jeder
        jedes jene jenem jenen jener jenes jetzt kann kein keine
        keinem keinen keiner keines können könnte machen man manche
        manchem manchen mancher manches mein meine meinem meinen
        meiner meines mit muss musste nach nicht nichts noch nun
        nur ob oder ohne sehr sein seine seinem seinen seiner seines
        selbst sich sie sind so solche solchem solchen solcher
        solches soll sollte sondern sonst über um und uns unsere
        unserem unseren unser unseres unter viel vom von vor während
        war waren warst was weg weil weiter welche welchem welchen
        welcher welches wenn werde werden wie wieder will wir wird
        wirst wo wollen wollte würde würden zu zum zur zwar zwischen
    """.split()),
    "EL": frozenset("""
        ο η το οι τα του της των τον την τους τις σε στο στη στην στους στις
        και κι ή ή ή αλλά μα όμως αν εάν ότι πως πώς αυτό αυτή αυτός αυτοί
        αυτές αυτά εγώ εσύ εμείς εσείς αυτοί αυτές μου σου του της μας σας
        τους με σε για από προς πριν μετά μέχρι ως όπως χωρίς εκτός εξ εκ
        ένας μία μια ένα δύο δυο τρία τρεις τέσσερις πέντε δεν μη μην ναι
        ίσως ποτέ πάντα ξανά πάλι κάθε όλα όλοι όλες όλος όλη όλους όλες
        κάποιος κάποια κάποιο μερικοί μερικές πολύ πολλά πολλές πιο πλέον
        ακόμα ακόμη επίσης μόνο μόνον τόσο τόση τόσοι τόσες πάνω κάτω εδώ
        εκεί τότε τώρα ωστόσο αφού επειδή ενώ άλλος άλλη άλλο άλλοι άλλες
        άλλα ίδιος ίδια ίδιο ίδιοι ίδιες ίδια έχω έχεις έχει έχουμε έχετε
        έχουν είχα είχες είχε είχαμε είχατε είχαν είμαι είσαι είναι είμαστε
        είστε είναι ήμουν ήσουν ήταν ήμασταν ήσασταν ήταν θα ότι ό,τι όποιος
        όποια όποιο γιατί διότι κατά πάνω μόλις μέσα στο μεταξύ έτσι λοιπόν
    """.split()),
    "EN": frozenset("""
        a about above after again against all am an and any are aren't as at
        be because been before being below between both but by can can't
        cannot could couldn't did didn't do does doesn't doing don't down
        during each few for from further had hadn't has hasn't have haven't
        having he he'd he'll he's her here here's hers herself him himself
        his how how's i i'd i'll i'm i've if in into is isn't it it's its
        itself let's me more most mustn't my myself no nor not of off on
        once only or other ought our ours ourselves out over own same shan't
        she she'd she'll she's should shouldn't so some such than that that's
        the their theirs them themselves then there there's these they they'd
        they'll they're they've this those through to too under until up very
        was wasn't we we'd we'll we're we've were weren't what what's when
        when's where where's which while who who's whom why why's with won't
        would wouldn't you you'd you'll you're you've your yours yourself
        yourselves
    """.split()),
    "ES": frozenset("""
        a al algo algunas algunos ante antes como con contra cual cuando
        de del desde donde durante e el ella ellas ellos en entre era erais
        eran eras eres es esa esas ese eso esos esta estaba estabais estaban
        estabas estad estada estadas estado estados estamos estando estar
        estaremos estará estarán estarás estaré estaréis estaría estaríais
        estaríamos estarían estarías estas este estemos estos estoy estuve
        estuviera estuvierais estuvieran estuvieras estuvieron estuviese
        estuvieseis estuviesen estuvieses estuvimos estuviste estuvisteis
        estuviéramos estuviésemos estuvo está estábamos estáis están estás
        esté estéis estén estés fue fuera fuerais fueran fueras fueron
        fuese fueseis fuesen fueses fui fuimos fuiste fuisteis fuéramos
        fuésemos fui fueron ha habida habidas habido habidos habiendo habrá
        habrán habrás habré habréis habría habríais habríamos habrían
        habrías habéis había habíais habíamos habían habías han has hasta
        hay haya hayamos hayan hayas hayáis he hemos hube hubiera hubierais
        hubieran hubieras hubieron hubiese hubieseis hubiesen hubieses
        hubimos hubiste hubisteis hubiéramos hubiésemos hubo la las le les
        lo los me mi mis mucho muchos muy más mí mía mías mío míos nada
        ni no nos nosotras nosotros nuestra nuestras nuestro nuestros o os
        otra otras otro otros para pero poco por porque que quien quienes
        qué se sea seamos sean seas seremos será serán serás seré seréis
        sería seríais seríamos serían serías seáis sido siendo sin sobre
        sois somos son soy su sus suya suyas suyo suyos sí también tanto
        te tendremos tendrá tendrán tendrás tendré tendréis tendría tendríais
        tendríamos tendrían tendrías tened tenemos tenga tengamos tengan
        tengas tengo tengáis tenida tenidas tenido tenidos teniendo tenéis
        tenía teníais teníamos tenían tenías ti tiene tienen tienes todo
        todos tu tus tuve tuviera tuvierais tuvieran tuvieras tuvieron
        tuviese tuvieseis tuviesen tuvieses tuvimos tuviste tuvisteis
        tuviéramos tuviésemos tuvo tuya tuyas tuyo tuyos tú un una uno
        unos vosotras vosotros vuestra vuestras vuestro vuestros y ya yo
        él éramos
    """.split()),
    "ET": frozenset("""
        ja ning ega või kuid aga kui sest et ka veel siis nüüd seal siia
        siit seda see selle sellele sellelt sellesse selles sellest sellega
        selleks sellena ma mu mind minu minus minust minuni minuna minuks
        meie meid meil meile meilt meis meist meiega meini sa sind sinu
        sinus sinust sinuni sinuna sinuks ta teda tema temas temast temani
        temana temaks teie teid teil teile teilt teis teist teiega teini
        nad neid nende neis neist nendega nendeks nendena olen oled on
        oleme olete pole polnud olla on ei mitte vaid niiet nõnda nii nagu
        ainult ka kohe juba enam veel ka lihtsalt nüüd siis tema oma omas
        kogu kõik kõike kõikidele igaüks igaühe igaühele igaühelt iga
        ükski ühel teisel teisele
    """.split()),
    "FI": frozenset("""
        ei eivät en et ette että hän hänen häneen hänellä häneltä hänelle
        hänestä hänet häntä he heidän heihin heillä heille heiltä heissä
        heistä heitä hänkin he ja jo joka jokin joko jolla jolle jolta jonka
        jossa josta jota jotain jotakin jotka jälkeen kanssa kuin kun ku
        ku se ne sitä siten siellä sieltä sinne siinä sinä sitten siitä siten
        siksi joko jollei jolloin jos kuitenkaan kuitenkin kunnes kuten
        ku me meidän meihin meillä meille meiltä meissä meistä meitä mihin
        mikä mikään mikäli millainen mille milloin minkä minä missä mistä
        miten mitkä mitä mitään mukaan myös ne nimittäin niiden niihin niillä
        niille niiltä niin niissä niistä niitä noiden noihin noilla noille
        noilta noin noissa noissa noista noita nyt näiden näin näissä
        näistä ole olemme ollut olisi olisivat olivat olla olleet ollut
        ollut ollut ollut olen olet olemme olette ovat oma omat on osa
        päälle se sen sentä siitä siksi sinusta sinä siellä sinne sinun
        siitä sitten suoraan suuri sä tai te teidän teihin teille teillä
        teiltä teissä teistä teitä tähän täällä tästä täten tällä tällä
        tämä tämän tänne tänä uusi vaan vaikka vai voi voida voidaan voinut
        ynnä yhdellä yhden yhteen yli ympärillä
    """.split()),
    "FR": frozenset("""
        a à au aux avec ce ces dans de des du elle en et eux il ils je
        la le les leur lui ma mais me même mes moi mon ne nos notre nous on
        ou par pas pour qu que quel quelle quelles quels qui sa sans se
        ses son sur ta te tes toi ton tu un une vos votre vous c d j l
        à c'est m n s t y été être suis es est sommes êtes sont sera
        seront serait étais était étions étiez étaient ai as a avons avez
        ont aura aurai aurait avais avait avions aviez avaient eu eus eut
        eûmes eûtes eurent ait aient été étant ayant fait faire faite faits
        plus aussi alors avant après autre encore peu très bien
    """.split()),
    "GA": frozenset("""
        a ach ag agus an aon ar arna as ba beirt bhúr caoga ceathair ceathrar
        chomh chuig chun cois céad cúig cúigear cúpla d daichead dar de deich
        deichniúr den dhá do don dtí dá dár dó dóibh dúinn faoi faoin
        fara fhearr fhéin fí fú gach gan go gur haon i iad idir in is le
        leis lena leo m mar mhúsáil mo na nach naoi naonúr ná ní nó nócha
        ochtar ocht ochtó os roimh sa san seacht seachtain seachtó seachtó
        seasca seisear shílfeá síos sé síos thar thri thrír tigh tré trí
        triúr trí tugaim tugair tugann tugann tugann tugann uimh um úsáid
    """.split()),
    "HR": frozenset("""
        a ako ali bi bih bila bili bilo bismo biste bit bog bok budem budeš
        bude budemo budete budu da do duž ga gledaj on ona ono oni one ja
        jer ji ju li me mi moj moja moje mu na nad nakon nam nas naš naša
        naše ne neka neki neko nekog nekoj nekom nemu ni ništa no o od
        on ona ono one oni op opčina op po pod ponovo prema prije pri
        s sa sam samo se si smo ste su svi sva sve svih svom svoj svoja
        svoje šta što ta te ti to tom toj toju u uz vam vas vi vrlo zar
        za zato zbog ću ćeš će ćemo ćete
    """.split()),
    "HU": frozenset("""
        a az egy ez ezt ezek ezen ezzel ezért és vagy de hogy nem is van
        volt lesz nincs minden semmi nincsen aki amely amelyik aki amit
        amelyet amelyek azon azonban annak annál ahhoz attól abban abból
        abba ahol ahonnan ahova ide oda itt ott most már még csak így úgy
        ilyenkor olyankor amikor mielőtt miután ha mert mivel mert hiszen
        ugyanis vagyis tehát ezért ezért tehát továbbá ráadásul valamint
        de mégis bár azonban viszont én te ő mi ti ők engem téged őt minket
        titeket őket nekem neked neki nekünk nektek nekik velem veled vele
        velünk veletek velük tőlem tőled tőle tőlünk tőletek tőlük rólam
        rólad róla rólunk rólatok róluk hozzám hozzád hozzá hozzánk hozzátok
        hozzájuk értem érted érte értünk értetek értük belém beléd belé
        belénk belétek beléjük rám rád rá ránk rátok rájuk vagyok vagy van
        vagyunk vagytok vannak voltam voltál volt voltunk voltatok voltak
        leszek leszel lesz leszünk lesztek lesznek minden mindegyik mindenki
        bármi bármilyen néhány több sok kevés kicsi nagy
    """.split()),
    "IT": frozenset("""
        a abbia abbiamo abbiano abbiate ad agl agli ai al all alla alle
        allo anche avemmo avendo avesse avessero avessi avessimo aveste
        avesti avete aveva avevamo avevano avevate avevi avevo avrai
        avranno avrebbe avrebbero avrei avremmo avremo avreste avresti
        avrete avrà avrò avuta avute avuti avuto c che chi ci coi col come
        con contro cui da dagl dagli dai dal dall dalla dalle dallo degl
        degli dei del dell della delle dello di dov dove e ebbe ebbero
        ebbi ed era erano eravamo eravate eri ero essendo faccia facciamo
        facciano facciate faccio facemmo facendo facesse facessero facessi
        facessimo faceste facesti faceva facevamo facevano facevate facevi
        facevo fai fanno farai faranno farebbe farebbero farei faremmo
        faremo fareste faresti farete farà farò fece fecero feci fece feci
        fece fece fece fossero fossi fossimo foste fosti fu fui fummo
        furono gli ha hai hanno ho i il in io l la le lei li lo loro lui
        ma mi mia mie miei mio ne negl negli nei nel nell nella nelle
        nello noi non nostra nostre nostri nostro o per perché però più
        può quale quali quanta quante quanti quanto quegli quei quel quella
        quelle quelli quello questa queste questi questo qui se sei senza
        si sia siamo siano siate siete sono sta stai stando stanno starai
        staranno starebbe starebbero starei staremmo staremo stareste
        staresti starete starà starò stava stavamo stavano stavate stavi
        stavo stemmo stesse stessero stessi stessimo steste stesti stette
        stettero stetti stia stiamo stiano stiate sto su sua sue sugl
        sugli sui sul sull sulla sulle sullo suo suoi tale tali ti tra
        tu tua tue tuo tuoi tutta tutte tutti tutto un una uno vai vi voi
        vostra vostre vostri vostro è
    """.split()),
    "LT": frozenset("""
        ant apie ar arba aš be bei bet bus būti būtent būtų buvo čia dėl
        dabar daugiau gali galima gana gerai gi i ir iš ją jeigu ji jie jis
        jiems jog joje jokia jokiam jokiame jokie jokiomis jokios jokiuose
        jūs jus jūsų jus juos jų ką kad kaip kai kalbėti kažkam kažkas
        kažkur ką kaltas kelias kelias keli kelis kelių keliuose kiek
        kitas kiti kitos kitomis kituose koks kokia kokiame kokie kokios
        kokiu kokiomis kuomet kur kuris kurie kuriame kurios kuriomis labai
        man manęs mano mes mums mus mūsų mūsiškis ne nei niekas niekur nors
        nuo o pa pat per po prie prieš prieš tai pripažinti reik reikia
        savo sako šie sa sis sis šis šitas šitie šituos taip tai tas tau
        tave tegu te toks tokia tokiame tokie tos tu tuos tuomet tuosvisai
        už vis visai visi visiems visus viskas vienas vienoje
    """.split()),
    "LV": frozenset("""
        a apakš ap ar arī bet bez bija bijis bijusi bijušas bijuši būs būt
        būtu daudz dažāds diez dēļ esam esat esi esmu gan gar grūti ielikt
        ik ir ja jau jeb jebkurš jebšu jo jūs jums jūsu kā kāds kāpēc kas
        kad kam kaut ko kopā kopš kura kuras kuri kurš lai labi maz man
        mani mans manuprāt mēs mēs mums mūsu nav ne nedaudz nedz neka
        nekad neko nekur nemaz nevis nez nu pa par patiešām pati pats pa
        pavisam pa pēc piekam piemēram pirmkārt pirms pār pār pārāk
        protams pār pār reiz sī šī šie šim šis šeit šī šim šie šādi šāds
        šo tad tādu tādēļ tāpēc tāds tālāk tas tās tev tevi tevis tu tā
        tādu tālāk tā tāpat te tev tas tām tām tāpēc tikko tikai tikko
        toreiz tomēr turklāt tu uz uzreiz vai var varbūt vēl vis visa
        visi visu visa vēlāk vairāk vairākas vairākiem vairākus
    """.split()),
    "MT": frozenset("""
        u w b f g il ma mhux mhux ta tal tas tat ġu ġie hu hi hawn hi
        huma kif kif jiena int aħna intom huma li ma mhux meta minn fuq
        għal wieħed waħda dak dik dawk dan din kull qed se ser ġej ġejja
        għax għaliex jew jekk lest tajjeb mhux baqa baqgħet baqgħu kien
        kienet kienu kienu issa lkoll naf taf jaf nafu tafu jafu sew
        żgur tal-istess għalhekk għalkemm bħal bħala bejn bejn taħt mingħajr
        ħafna ftit żgħir kbir kif xi għandu għandha għandhom mhux nieħu
        nista jista tista nistgħu tistgħu jistgħu kollox xejn dejjem qatt
    """.split()),
    "NL": frozenset("""
        aan af al alles als altijd andere ben bij daar dan dat de der deze
        die dit doch doen door dus een eens en er ge geen geweest haar
        had heb hebben heeft hem het hier hij hoe hun iemand iets ik in is
        ja je kan kon kunnen maar me meer men met mij mijn moet na naar
        niet niets nog nu of om omdat ons ook op over reeds te tegen toch
        toen tot u uit uw van vóór voor want waren was wat we wel werd
        wezen wie wij wil worden zal ze zei zelf zich zij zijn zo zonder
        zou
    """.split()),
    "PL": frozenset("""
        a aby ach acz aczkolwiek aj albo ale alez ależ ani az aż bardziej
        bardzo beda bedzie bez deda będą bede będę bedzie będzie bo bowiem
        by byc być byl byla byli bylo była było bym bynajmniej cala cale
        cali caly całe cała cały chce chcę chociaż ci cie ciebie cię co
        cokolwiek cos coś czasami czasem czemu czy czyli daleko dla dlaczego
        dlatego do dobrze dokad dokąd dosc dość duzo dużo dwa dwaj dwie
        dwoje dzis dzisiaj dziś gdy gdyby gdyz gdyż gdzie gdziekolwiek
        gdzies gdzieś go ich ile im inna inne inny innych iz iż ja ją jak
        jakas jakaś jakby jaki jakichś jakie jakis jakiś jakiż jakkolwiek
        jako jakos jakoś je jeden jedna jednak jednakze jednakże jedno
        jego jej jemu jest jestem jesli jeszcze jeśli jezeli jeżeli juz
        już kazdy każdy kiedy kilka kims kimś kto ktokolwiek ktora ktore
        ktorego ktorej ktory ktorych ktorym ktorzy która które którego
        której który których którym którzy ku lat lecz lub ma mają mam
        mi miedzy między mimo mna mną mnie moga mogą moi moim moj moja
        moje moim mój może mozliwe możliwe mozna można my na nad nam nami
        nas nasi nasz nasza nasze nawet nia nią nic nich nie niech niej
        niemu nigdy nim nimi niz niż no o obok od około on ona one oni
        ono oraz oto owszem pan pana pani po pod podczas pomimo ponad
        poniewaz ponieważ powinien powinna powinni powinno poza prawie
        przeciez przecież przed przede przedtem przez przy roku rowniez
        również sam sama są sie się skad skąd soba sobą sobie sposob sposób
        swoje ta tak taka taki takich takie tako takze także tam te tego
        tej ten teraz też to toba tobą tobie totez toteż totobą trzeba
        tu tutaj twoi twoim twoj twoja twoje twoim twój ty tych tylko tym
        u w wam wami was wasi wasz wasza wasze we według wiele wielu więc
        więcej wlasnie właśnie wszyscy wszystkich wszystkie wszystkim
        wszystko wtedy wy z za zaden zadna zadne zadnych żaden żadna żadne
        żadnych zapewne zawsze ze że zeby żeby zeznowu zł znow znowu znów
        zostal został
    """.split()),
    "PT": frozenset("""
        a à acho ainda algumas alguns ali ano antes ao aos apenas as às
        assim até atrás através bem boa bom cada coisa coisas com como contra
        da das de dela delas dele deles depois desde dessa dessas desse
        desses desta destas deste destes dia dias diante disso diz dizem
        do dos durante e é ela elas ele eles em entre era essa essas esse
        esses esta estamos estão estar estas estava estavam este estes estive
        estiveram esto estou eu fala falar falou faz fazer fez fim foi fomos
        for foram fosse fui há houve isso isto já lhe lhes lo logo mais mas
        me mesma mesmo meu meus minha minhas muita muitas muito muitos na
        não nas nem nessa nessas nesse nesses nesta nestas neste nestes nisto
        no nos nós nossa nossas nosso nossos num numa o os ou outra outras
        outro outros para pela pelas pelo pelos perto pode poder podia pois
        por porque pouca poucas pouco poucos primeira primeiro próximo
        próxima próximo qual quando quanta quantas quanto quantos que quem
        quer quero sao são se sem sempre seu seus si sido só sob sobre
        somos sou sua suas talvez também tão te tem tendo tens ter teu teus
        teve tinha tinham toda todas todo todos tu tua tuas tudo um uma
        umas uns vai vamos vão você vocês vou
    """.split()),
    "RO": frozenset("""
        acea aceasta aceea acel acelaşi acea aceea acei aceia acele aceleaşi
        acelei acelor acest acesta acestea acestei acestia acesti aceşti
        aceştia acolo acord acum ai aia aibă aici al ăla ale alea ălea
        altceva altcineva am ar are aş aşadar asemenea asta ăsta astăzi
        ăştia astfel asupra atare atât atâta atâtea atâţia atunci au avea
        avem aveţi azi bine bucur bună ca că căci când care căror căruia
        cărui cât câte câţi cătârva către câtva ce cea cealaltă cei ceilalţi
        cel cele celelalte celor ceva chiar cinci cînd cine cineva cit
        cîte cîţi cîtva cu cum cumva curând curînd da dă daca dacă dat
        datorită dau de deasupra deci deja deoarece departe deşi din dintr
        dintre doi doilea două drept după ea ei el ele eram este eşti eu
        face fără fata fi fie fiecare fii fim fiţi fiu frumos graţie halo
        iar ieri îi îl îmi împotriva în înainte înaintea încât încît încotro
        între întrucît întrucât îţi la lângă le li lîngă lor lui mă mai
        mâine mea mei mele mereu meu mi mie mîine mine mult multă mulţi
        mulţumesc ne nevoie nici nicăieri nimeni nimeri nimic nişte noastră
        noastre noi noroc noştri nostru nouă nu opt ori oricând oricare
        oricât orice oricine oricum oricând oricât pa până pe pentru peste
        pic poate pot prea prima primul prin printr-o printre puţin rog
        sa să săi sale sau său se şi sînt sînteţi spate spre sub sunt
        suntem sunteţi ta tăi tale tău te ţi ţie timp tine toată toate
        tot toti toţi totuşi tu un una unde undeva unei uneia unele uneori
        unii unor unora unu unui unuia unul vă vâi vi voastră voastre voi
        voştri vostru vouă vreo vreun zece zero zi zice
    """.split()),
    "SK": frozenset("""
        a aby aj ak akže ale alebo ani áno asi až ba bez bo budem budeme
        budete budeš budú by byť cez čez či čo čokoľvek čoraz čože ďakujem
        dnes do doteraz dovtedy dva dve ho hoci i ich im iný ja jeho jej
        ju k každý keď keďže kto ktorý ku kúsok len lenže ľudia ma má majú
        mal mala mali mám máme máš medzi mi mna mne mnoho moja moje mojej
        mojich mojím mojou my na nad nám nami nás náš naša naše naši nech
        nej nemôže nemu nemá nepôjde než nič niečo nie nikdy ničoho ničom
        nim ním nimi nimi no o od oboch on ona oni ono opäť ostatne pod
        podľa pomocou pravda pre pred predo preto prečo pri raz s sa sám
        samé si sme so spolu sú svoja svoje svojich svoju svojím svojej
        ta tá tak taká tákú také taký takže tam tej teba tebe tebou ten
        tento tí ti tie tiež tieto tisíc to toho tom tomto totiž tu tvoj
        tvoja tvoje tvojej tvojich tvojím tvoju ty tých tým týmto u už v
        vám vás váš vy vždy z za zatiaľ zatiaľ že žiadne žiaľ
    """.split()),
    "SL": frozenset("""
        a ali b bi bil bila bile bili bilo biti blizu bo bodo bodisi bolj
        bom bomo boste bova boš brez c cel cela celi celo č če često ći
        čigav čigava čigavo čimer čisto da daleč dan danes deset deveta
        deveti deveto devet do dober dobra dobro dokler dol dovolj drug
        druga drugo dva dve eden edina edini eden ena ene eni enkrat eno
        etc f g g. gor h ha haha he hej i in iv iz ja jaz je ji jih jim
        jo jutri k kadar kadarkoli kaj kajti kak kakor kakšen kakšna
        kakšno kakšne kako kakor kamor kamorkoli kar karkoli katera katere
        kateri katero kdaj kdo kdorkoli ker ki kje kjer kjerkoli ko koder
        kodorkoli koliko komu kot kratek kratka kratke kratki l le lep
        lepa lepe lepi lepo leta letos lih m majhen majhna majhni mali
        manj me med medtem mene mesec metr mi midva midve mnogo moj moja
        moje mora morajo moram moramo morata morate morem moreš morejo
        morete moreš morem morete morata moramo morata morate moreta moremo
        moreta morete morem moreva moreva moreva morete morejo morem morete
        morata moramo morate moreta morete moreva morejo morem moreta morem
        morem moreta morete moreta morete morata moramo morate morejo
    """.split()),
    "SV": frozenset("""
        aderton adertonde adjö aldrig alla allas allt alltid alltså än
        andra andras annan annat ännu artonde artonn att åtminstone åtta
        åttio åttionde åttonde av även båda bådas bakom bara bäst bättre
        behöva behövas behövde behövt beslut beslutat beslutit bland blev
        bli blir blivit bort borta bra dag dagar dagarna dagen där därför
        de del delen dem den deras dess dessa det detta dig din dina dit
        ditt dock du efter eftersom elfte eller elva en enkel enkelt enkla
        enligt er era ert ett ettusen fanns få fanns far fått femte femtio
        femtionde femton femtonde fick fin finnas finns fjärde fjorton
        fjortonde fler flera flesta fram framför från fyra fyrtio fyrtionde
        gå gälla gäller gällt går gärna gått genast genom gick gjorde gjort
        god goda godare godast gör göra gott ha hade haft han hans har
        här heter hit hög höger högre högst hon honom hundra hundraen
        hundraett hur i ibland icke idag igår igen imorgon in inför inga
        ingen ingenting inget innan inne inom inte inuti ja jag jämfört
        kan kanske knappast kom komma kommer kommit kr kunde kunna kunnat
        kvar länge längre långsam långsammare långsammast långsamt längst
        långt lätt lättare lättast legat ligga ligger lika likställd
        likställda lilla lite liten litet man många måste med mellan men
        mer mera mest mig mindre minst mitt mittemot möjlig möjligen
        möjligt möjligtvis mot mycket någon någonting något några när
        nästa ned nederst nedersta nedre nej ner ni nio nionde nittio
        nittionde nitton nittonde nödvändig nödvändiga nödvändigt
        nödvändigtvis nog noll nr nu nummer och också ofta oftast olika
        olikt om oss över övermorgon överst övre på rakt rätt redan så
        sade säga säger sagt samma sämre sämst sedan senare senast sent
        sex sextio sextionde sexton sextonde sig sin sina sist sista
        siste sitt sjätte sju sjunde sjuttio sjuttionde sjutton sjuttonde
        ska skall skulle slutligen små smått snart som stor stora större
        störst stort tack tidig tidigare tidigast tidigt till tills tillsammans
        tio tionde tjugo tjugoen tjugoett tjugonde tjugotre tjugotvå tjungo
        tolfte tolv tre tredje trettio trettionde tretton trettonde två
        tvåhundra under upp ur ursäkt ut utan utanför ute vad vänster
        vänstra var vår vara våra varför varifrån varit varit varken värre
        värst vart vårt vem vems verkligen vi vid vidare viktig viktigare
        viktigast viktigt vilka vilkas vilken vilket vill
    """.split()),
}


def get_stopwords(lang: str) -> frozenset[str]:
    """Return the stopword set for the given CPV language code."""
    return STOPWORDS.get(lang, frozenset())
