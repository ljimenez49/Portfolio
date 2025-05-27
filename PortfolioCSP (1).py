#Lizbeth Jimenez and George Ibarra
#Period 3
#3/19/25
#AP CSP CREATE Project

#Initialize
import random
#Arrangements, E. (2023, April 16). 50 most popular types of flowers to give or grow - Edible® blog. Edible® Blog. https://www.ediblearrangements.com/blog/types-of-flowers/?srsltid=AfmBOopk_TdxSihFiPPhj9N1P0YmfVRKFYnCb5fHE5ty77GMfIdEvaR9
#Utilizing: We are using the list of flowers provided by this source, additionally we are utilizing the information + description for every type of flower listed.



flowers = ["Alstroemeria"," Calla Lily"," Daisy"," Gardenia"," Carnation"," Gerbera Daisy"," Orchid"," Tulip"," Peony"," Dahlia"," Marigold"," Aster"," Azalea"," Buttercup"," Chrysanthemum"," Geranium"," Delphinium"," Lavender"," Snapdragon"," Zinnia"," Iris"," Rose"," Sunflower"," Poppy"," Periwinkle"," Crocus"," Black-eyed Susan"," Daffodil"," Petunia"," Ranunculus"," Violet"," Dusty Miller"," Hyacinth"," Begonia"," Camellia"," Clematis"," Coneflower"," Evening Primrose"," Forget Me Not"," Forsythia"," Freesia"," Gladiolus"," Hellebore"," Hibiscus"," Hydrangea"," Jasmine"," Lilac"," Poinsettia"," Queen Anne's Lace"," Rhododendron"]

description = ["The alstroemeria, also called the Peruvian lily, features streaked or speckled blossoms in a range of colors, including white, yellow, orange, pink, and red. With their trumpet-like appearance, they resemble lilies and grow to one to three feet tall. ",
"Calla lilies come in a variety of different colors, from snow white to bright pink. They feature a beautiful trumpet shape with smooth, sword-like foliage.",
"Daisies are a bright and fun flower. The petals come in a variety of colors, including white, blue, and lavender. Daisies feature a yellow central disc with a long stem.",
"Notable for their wax-like appearance and oval-shaped leaves, gardenia flowers range from pale yellow to creamy white. Gardenias are also known for their sweet scent.",
"A double layer of petals with crinkly edges are the chief characteristics of carnations. They come in a wide variety of colors and can be dyed to practically any color and shade on earth.",
"Gerbera daisies are daisy-like flowers that come in bright colors, including pink, red, yellow, orange, and salmon. They have a long vase life and are one of the most used cut flowers in the world.",
"Orchid flowers include several notable features, including three petals, three sepals, and a single lip that extends, which is known as a labellum. Orchids also have a waxy tube-like structure in the center of the flower called a column.",
"Tulips have ruffled petals with streaks of colors and are available in a variety of colors including pink, red, yellow, orange, purple, and white. There are a wide variety of types of tulips, and they are often cultivated to achieve different characteristics.",
"Peonies have large, wonderfully fragrant flowers, in colors including everything from purple and pink to darker shades of red. They have a short blooming season, which only lasts about a week or so.",
"In a rainbow of colors, dahlia flowers range from two-inch blooms to giant blossoms that measure up to 15 inches. Most types grow four to five feet tall.",
"Most marigold flowers are yellow to deep orange. They typically feature a cluster of petals closely bunched together that resembles a pompom with dark green foliage.",
"Blooming in late summer and early fall, asters come with a bright yellow center and a variety of petal hues, including blue, purple, pink, and white. They attract bees and butterflies and are an important source of late-season nectar.",
"The leaves, size, and shape of azaleas vary greatly by variety, and they range in color from pink to red to salmon. Azaleas are flowering shrubs in the rhododendron family, but not all rhododendrons are azaleas.",
"Buttercups feature single or loosely clustered flowers with yellow petals and green foliage. Buttercups usually flower in the spring, but you can sometimes find flowers throughout the summer.",
"Chrysanthemums are staples in fall gardens. They are best known for their bright flowers in every color of the rainbow and a full, dramatic display of blooms in a round semi-circle above the foliage.",
"A classic garden plant, geranium flowers have five petals in white, pink, purple, or blue. They’re relatively easy to grow, so they’re a favorite of gardeners to plant in flower beds, along borders, and in containers.",
"Delphiniums are known for their large spikes of colorful flowers in bright shades of blue, pink, white, and purple. They’re more challenging to grow than other types of flowers because they don’t like hot, dry weather.",
"Lavender is known for its fragrance, medicinal properties, and beautiful bluish-purple color. it blooms in the summer months and is a favorite of bees and butterflies.",
"Snapdragons can range from six inches to three feet depending on the variety. Flowers grow on tall, narrow spikes above the foliage and come in all colors of the rainbow from pastel tones to bold, saturated colors.",
"Zinnia blooms are multi-colored in shades of yellow, orange, white, red, pink, purple, and more. They also come in a wide variety of appearances, including a single row of petals and a luscious dome shape. They range in size from about a foot to over three feet tall.",
"Iris flowers have an unusual, but beautiful appearance with the color purple. The petals resemble a fleur-de-lis, with some petals standing straight up while others slope down atop long, erect stems.",
"Roses are perhaps the most popular cut flower for floral displays. They feature a tight coil of petals that range in color from white to tones of yellow, pink, and dark crimson and have a delightful fragrance.",
"With brilliant yellow petals and a brown to black central disc, sunflowers are practically unmistakable. Their bright and happy appearance resembles the sun, making them a crowd favorite in the summer months.",
"Bright red in color with big, showy flowers and feathery green foliage, poppies are a beautiful flower. Poppies are also commonly often worn on Memorial Day to honor fallen soldiers.",
"Periwinkle is often used by gardeners as an evergreen ground cover due to its dark green foliage. Its flowers are purple, blue, or white, depending on the variety.",
"Crocuses bloom bright and early in the spring (sometimes they even poke through the snow) and lead the way for other springtime flowers to emerge. They come in purple, blue, yellow, pink, and white and grow low to the ground.",
"Black-eyed Susans are known for their bright yellow petals and brownish-black, dome-shaped center. They bloom in late summer and grow on long stems that can reach four feet in height.",
"Bright and fragrant flowers, daffodils bloom early in the spring. The blossoms feature six petals and a trumpet in the middle and are typically a combination of bright yellow and white.",
"In all shades from bright white to deep purple or red, Petunias bloom profusely from early summer until frost. They’re one of the easiest flowers to grow, making them perfect for containers, flower beds, borders, and so much more.",
"Ranunculus come in all shades of warm colors, from yellow and red to purple and pink. Their blooms burst open to feature rows upon rows of petals with a beautiful and striking appearance.",
"Violets typically have heart-shaped leaves and asymmetrical flowers that vary in color among the different varieties. Many are violet as their name suggests, but some are also blue, white, or yellow.",
"With its distinctive silver and lacy foliage, the Dusty Miller is a favorite of gardeners. Its blooms are bright yellow and stand out in a striking way against the backdrop of silver.",
"Hyacinth is a hardy perennial with distinctive flowers that rise on an erect stalk. It features a pleasant fragrance and is a favorite for Easter displays due to its early spring blooms.",
"Begonias come in several varieties and range in size from as small as six inches to nearly three feet tall. Typically, begonias have white, pink, or red flowers, but cultivators have created a more diverse spectrum of colors, including yellow and orange.",
"Camellia flowers are large and showy with a rose-like appearance in colors ranging from white to pink, red, and yellow. Camellias are known to symbolize love, affection, and admiration.",
"The clematis vine features a spectacular show of white, blue, violet, or purple flowers. It can grow up to 12 feet tall if provided the opportunity to climb on a trellis, arbor, fence, or wall.",
"Coneflower has large flowers with spiny, dome-shaped, orange or brown centers that grow on sturdy stalks reaching up to five feet in height. They come in a variety of colors, including purple, orange, red, and white.",
"Evening Primrose is a tall wildflower that blooms at sunset. The flower is yellow on the outside and whitish within and quickly fades in bright sunlight.",
"Forget me nots are always recognizable by their deep blue petals contrasted with a bright yellow center. They have bright green foliage, which contrasts nicely with their blue blooms.",
"Forsythias are shrubs that can grow up to ten feet tall and twelve feet across. They bloom from early to mid-April and feature four-petaled flowers in shades ranging from light yellow to bright golden yellow.",
"Freesia flowers are funnel-shaped flowers that form a one-sided spike on top of the plant. Freesia blooms can range from yellow to orange or pink to red, and they emit a sweet, citrusy scent.",
"Gladiolus features a tall, striking stalk of purple blooms with a fragrant scent. Named after gladiators’ swords, gladiolus is typically known to symbolize remembrance, faithfulness, and loyalty.",
"Hellebore features exquisite bowl-shaped flowers in white, pinks, yellows, and reds. They feature sturdy stems that are serrated like a knife along the edges.",
"Hibiscus features trumpet-shaped flowers that come in a range of colors like red, pink, and white and can grow as large as a paper plate, reaching six inches in diameter. They typically grow in tropical climates and don’t fare well in cooler temperatures.",
"Hydrangeas are popular with gardeners and florists due to their large, round flower heads comprised of tiny, individual flowers. They come in a wide variety of colors, including blue, purple, and white.",
"Jasmine grows as a bushy shrub or climbing vine and produces tubular, waxy-white flowers and oval, shiny leaves. The flowers emit a rich, sweet, and sensual fragrance that’s used in perfumes across the globe.",
"Lilacs are easily recognized by their long, cone-shaped blooms covered in tiny, tubular flowers. They’re best known for their lilac-colored blooms but also come in white, blue, pink, and yellow.",
"Poinsettias are the classic Christmas flower because of their bright red appearance. The bright petals aren’t actually flowers, but instead are the upper leaves of the plant.",
"Queen Anne’s Lace is most identifiable by its white, lacy flowers, and oftentimes the flower has a solitary purple dot in the center. In fact, the plant earned its name from a legend that Queen Anne of England pricked her finger and a drop of blood landed on the white lace she was sewing.",
"Rhododendrons have large, bell-shaped flowers that grow in clusters in a wide variety of colors, including purple, red, orange, white, pink, and yellow. They grow best in shaded areas and feature evergreen foliage in greenish-blue or green.",]

ribbon = ["red","white","black","blue","light-blue","green","dark-green","pink","baby-pink","purple","orange","yellow","lime-green","dark-blue","violet","cyan","light-purple","Fuschia","Brown","Silver","Gold"]

wrapping = ["Brown","Black","White","Clear","Pink"]

list = []
list2 = []

#Functions
def flowerChoice():
    print("Welcome to our Online Flower Bouquet generator! Here you can customize any bouquet from the flower to the wrapping papper and you can't forget the ribbon!")
    choice = input("Briefly describe the flowers you are looking for today in one world?")
    for i in range(len(description)):
        if choice in description[i]:
            list.append(flowers[i])
            list2.append(description[i])
    print(list)
    print(list2)
    for i in range(len(list)):
        print(list[i])
        print(list2[i])


def wrappingPaperChoice():
    print("Next, choose which kind of wrapping paper you wish to use for your bouquet!")
    answer = input("Choose from our following options: Brown, Black, White, Clear, Pink, random")
    if answer == "random":
        random_item = random.choice(wrapping)
        print(random_item + "! amazing choice, this bouquet is looking amazing so far!")
    else:
        answer == "Brown" or "Black" or "White" or "Clear" or "Pink"
        print(answer + "! amazing choice, this bouquet is looking amazing so far!")


def ribbonChoice():
    print("Finally, it is time to choose the color of your ribbon, you have many options here")
    answer = input("Choose from our following options: red , white , black , blue , light-blue ,lime-green, dark-blue, violet, cyan, light-purple, Fuschia, Brown, Silver, Gold, random")

    if answer == "random":
        random_item = random.choice(ribbon)
        print("Your random ribbon color is..." + random_item + "! amazing color, this bouquet is almost done, get excited!")

    else:
        print(answer + "! amazing choice, this bouquet is almost done, get excited!")


def bouquetMaker(count):
    for i in range(count):
        flowerChoice()
        wrappingPaperChoice()
        ribbonChoice()
        print("Here is your " + str(count) + " bouquet, so stunning!" )
        print("Your bouquet will be an arrangment of these flowers: " + str(list))







#Main
bouquetMaker(2)
