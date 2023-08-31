from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie



# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Astronomy Max", page_icon="🪐", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- HEADER SECTION ----
with st.container():

 st.subheader("Where Astronomy meets Fun and AI 🪐🤖")
st.title("Astronomy Max")
st.write("A Place For Learning About Space,Tech,Science With the help of AI👽👾")
st.write("An MBA Original made by Burak Arslan")
st.write("[My IG➡](https://www.instagram.com/mad_bro1/)")

# ---- What You Can Find Here ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What You Can Find Here")
        st.write("##")
        st.write(
            """
            
            In this site you will be able to find:
             - The latest Astronomy related news.
              - Cool things related to science 
             - Other stuff i thought was cool enough to be included.
             - Along with a self built AI Chatbot "Alsephina.ai" , which can help you with almost 😉
              any question you may have which will be added very soon.
              The goal will always be to make learning as fun as possible.
              - ( This site was made by one person alone so it still may have issues which will be fixed asap)
              """
            )

        #  = ---- LOAD ASSETS ----
        lottie_coding = load_lottieurl("https://lottie.host/070baa4e-a368-4d5d-ac5f-10715119601e/UnPenffxHo.json")
        img_contact_form = Image.open("images/yt_img_contact_form.png")
        img_black_hole = Image.open("images/yt_img_black_hole.png")
        img_exo_planet = Image.open("images/img_exo_planet.png")
        img_rocket_pic = Image.open("images/img_rocket_pic.png")
        img_planet_nine = Image.open("images/img_planet_nine.png")
        img_white_hole = Image.open("images/img_white_hole.png")
        img_multiverse_pic = Image.open("images/img_multiverse_pic.png")
        img_planet_pic = Image.open("images/img_planet_pic.png")
        img_ccylical = Image.open("images/img_ccylical.png")
        abd_ufo = Image.open("images/abd_ufo.png")
        grandpa_paradox = Image.open("images/grandpa_paradox.png")
        Mercury_in_true_color = Image.open("images/Mercury_in_true_color.png")
        venus2_pic = Image.open("images/venus2_pic.png")
        earth_pic = Image.open("images/earth_pic.png")
        mars_pic = Image.open("images/mars_pic.png")
        jupiter_pic = Image.open("images/jupiter_pic.jpg")
        Saturn_pic = Image.open("images/Saturn_pic.png")
        Uranus_pic = Image.open("images/Uranus_pic.png")
        neptune_pic = Image.open("images/neptune_pic.png")
        pluto_pic = Image.open("images/pluto_pic.png")
        the_sun_pic = Image.open("images/the_sun_pic.png")
        Solar_System_Scale = Image.open("images/Solar_System_scale.png")
        Solar_System_distance_to_scale = Image.open("images/Solar_System_distance_to_scale.png")
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/style.css.css")
    with right_column:
        st_lottie(lottie_coding, height=300, key="space")

        # ---- LATEST SPACE NEWS ----
        with st.container():
            st.write("---")
st.header("Latest Astronomy & Space News")
st.write('##')
image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(img_contact_form)
with text_column:
    st.subheader("Indian rover begins exploring moon's south pole")
    st.write(
        """        
        India began exploring the moon's surface with a rover on Thursday, a day after it became the first nation to land a craft near the largely unexplored lunar south pole.
Pragyan—"Wisdom" in Sanskrit—rolled out of the lander hours after the latest milestone in India's ambitious but cut-price space program sparked huge celebrations across the country.
"Rover ramped down the lander and India took a walk on the moon!" the Indian Space Research Organisation (ISRO) posted on X, formerly known as Twitter, on Thursday.
The six-wheeled, solar-powered rover will amble around the relatively unmapped region and transmit images and scientific data over its two-week lifespan.
"""
    )
    st.markdown("[Source➡](https://phys.org/news/2023-08-indian-rover-exploring-moon-south.html)")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
          st.image(img_black_hole)
with text_column:
 st.subheader("Black Hole Destroyed a Star and Threw the Pieces Into Space")
st.write(
    """
NASA’s Chandra X-ray Observatory and ESA’s XMM-Newton telescope both captured the X-ray spectra of the event, and further observations from other observatories provided UV spectra. Together, this gave astronomers a detailed look at the composition of the doomed star. In this recent work, the team was able to analyze the spectra of both the material captured in orbit around the black hole and gasses that streamed away from the black hole. By comparing things such as the abundances of nitrogen and carbon in the stellar debris, the team was able to confirm the star had a mass of about 3 Suns.
Earlier this year, astronomers observed another TDE named Scary Barbie which could have been a 14 solar mass star, but this estimate is based on the overall brightness of the event, not its spectra. ASASSN-14li is currently the largest TDE with a confirmed mass.
This event is a powerful example of how stars near a supermassive black hole. With further events, we may even be able to study the clustering of stars around supermassive black holes in other galaxies, which would help us understand how the central cores of galaxies can evolve and the role they play in stellar evolution.
"""
)

st.markdown("[Source➡](https://www.universetoday.com/162921/a-giant-black-hole-destroyed-a-star-and-threw-the-pieces-into-space/#more-162921)")
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_exo_planet)
    with text_column:
        st.subheader("TESS has found thousands of possible exoplanets")
        st.write(
            """
            There are more than 5,000 confirmed exoplanets in our galaxy. That number is going to rise significantly in the next decade.
             The Transiting Exoplanet Survey Satellite (TESS) has already cataloged more than 4,000 candidate exoplanets,
             and the PLAnetary Transits and Oscillations of stars (PLATO) is scheduled to launch in 2026.
We will soon have more than 10,000 worlds where life might be able to survive.
 It's an amazing idea, but with so many exoplanets we don't have the resources to search for life on all of them.
 So how do we prioritize our search?
 That's the focus of a recent paper on the pre-print server arxiv. In it, the team strives to identify the "best in class" candidates for exoplanets that could be further studied by the spectroscopic cameras of the James Webb Space Telescope (JWST).
  Their list could not only help astronomers find evidence of life but also help us understand the range of atmospheres exoplanets have.
To generate their best choices, the team sorted both known and candidate exoplanets into a category grid arranged by planet radius and estimated surface temperature.
Within each category, they then ranked exoplanets by a transmission spectroscopy metric (TSM) and emission spectroscopy metric (ESM).
 In other words, those exoplanets with the best chance of having detectable transmission or emission spectra. Since TSM and ESM only focus on the strength of the spectrum relative to the background noise, the team further refined their ranking by the potential for spectra to be detectable using current observatories. (Click the source to read the fully detailed story.)
 """
        )
    st.markdown("[Source➡](https://phys.org/news/2023-08-tess-thousands-exoplanets-jwst.html)")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_rocket_pic)
    with text_column:
        st.subheader("NASA’s SpaceX Crew-7 Launches to International Space Station")
        st.write(
            """
            An international crew of four representing four countries is in orbit following a successful launch to the International Space Station at 3:27 a.m. EDT Saturday, Aug. 26, from Launch Complex 39A at NASA’s Kennedy Space Center in Florida.
             The agency’s SpaceX Crew-7 mission is the seventh commercial crew rotation mission for NASA.
A SpaceX Falcon 9 rocket launched the Dragon spacecraft into orbit carrying NASA astronaut Jasmin Moghbeli, ESA (European Space Agency) astronaut Andreas Mogensen, JAXA (Japan Aerospace Exploration Agency) astronaut Satoshi Furukawa, and Roscosmos cosmonaut Konstantin Borisov, for a science expedition aboard the orbital laboratory.
“Crew-7 is a shining example of the power of both American ingenuity and what we can accomplish when we work together,” said NASA Administrator Bill Nelson.
 “Aboard station, the crew will conduct more than 200 science experiments and technology demonstrations to prepare for missions to the Moon, Mars, and beyond, all while benefitting humanity on Earth.
 By partnering with countries around the world, NASA is engaging the best scientific minds to enable our bold missions, and it’s clear that we can do more – and we can learn more – when we work together.”
 """
        )
        st.markdown("[Source➡](https://www.nasa.gov/press-release/nasa-s-spacex-crew-7-launches-to-international-space-station)")

# ---- THEORIES ----
with st.container():
 st.write("---")
st.title("Theories:")
st.subheader("🚀🦸‍♂️A Collection of Space-Science related Theories i find interesting👽🚀")
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_planet_nine)
        with text_column:
            st.subheader("Planet 9/X")
            st.write(
                """
                Entirely depends whether you count Pluto as a Planet or Dwarf Planet,
                the Planet X (or otherwise known as Planet 9) theory is not as hard to believe as the 
                other space related theories as it is a likely possibility it exists. However its still not confirmed or denied so
                Here is some information about it:
                Caltech researchers have found mathematical evidence suggesting there may be a "Planet X" deep in the solar system. This hypothetical Neptune-sized planet orbits our Sun in a highly elongated orbit far beyond Pluto.
                 The object, which the researchers have nicknamed "Planet Nine," could have a mass about 10 times that of Earth and orbit about 20 times farther from the Sun on average than Neptune.
                 It may take between 10,000 and 20,000 Earth years to make one full orbit around the Sun.
                 The idea of another unknown Planet we dont know much about excites me, Although it being even more unlikely the planet may even contain life.
                 Who are we to say the opposite without any evidence?
                 (Click the source for more information about this hypothetical planet)
                 """
            )
            st.markdown("[Source➡](https://solarsystem.nasa.gov/planets/hypothetical-planet-x/in-depth/#:~:text=This%20hypothetical%20Neptune%2Dsized%20planet,Sun%20on%20average%20than%20Neptune.)")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
          st.image(img_white_hole)
          with text_column:
              st.subheader("White Holes")
              st.write(
                  """
                  White holes are the theoretical opposites of black holes. They are theorized to exist based on the very same math and general relativity concepts as black holes, although we have yet to identify a stable example in the universe. If you were to observe a white hole from a distance,
                   it would look very much like a black hole functioning in reverse, with light and matter slowly spewing outwards from what would otherwise look like a black hole. It is theorized that nothing is able to penetrate past a white hole’s event horizon,
                    just as nothing can escape from within a black hole’s event horizon.
                    
                    
                    
                    """

              )
              with st.container():
                  st.write("---")
                  image_column, text_column = st.columns((1, 2))
                  with image_column:
                      st.image(img_multiverse_pic)
                      with text_column:
                          st.subheader("The Multiverse")
                          st.write(
                              """
                              Similar to the theories before, this theory is also more likely to be true compared to most space theories out there, Now lets get to what this term "Multiverse" is.
                               The Multiverse is the hypothetical set of all universes. Together, these universes are presumed to comprise everything that exists: the entirety of space, time, matter, energy, information, and the physical laws and constants that describe them.
                                The different universes within the multiverse are called "parallel universes", "other universes", "alternate universes", or "many worlds".
                               One common assumption is that the multiverse is a "patchwork quilt of separate universes all bound by the same laws of physics.
The concept of multiple universes, or a multiverse, has been discussed throughout history, with origins in ancient Greek philosophy.
 It has evolved over time and has been debated in various fields, including cosmology, physics, and philosophy. Some physicists argue that the multiverse is a philosophical notion rather than a scientific hypothesis, as it cannot be empirically falsified.
 In recent years, there have been proponents and skeptics of multiverse theories within the physics community.
 Although some scientists have analyzed data in search of evidence for other universes, no statistically significant evidence has been found.
  Critics argue that the multiverse concept lacks testability and falsifiability, which are essential for scientific inquiry, and that it raises unresolved metaphysical issues.
"""

                          )
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((4, 2))
        with image_column:
            st.image(img_ccylical)
        with text_column:
            st.subheader("Big Bounce")
            st.write(
                """
                The Big Bounce is a hypothesized cosmological model for the origin of the known universe. It was originally suggested as a phase of the cyclic model or oscillatory universe interpretation of the Big Bang, where the first cosmological event was the result of the collapse of a previous universe. 
                It receded from serious consideration in the early 1980s after inflation theory emerged as a solution to the horizon problem, which had arisen from advances in observations revealing the large-scale structure of the universe.
                 In the early 2000s, inflation was found by some theorists to be problematic and unfalsifiable in that its various parameters could be adjusted to fit any observations, so that the properties of the observable universe are a matter of chance.
                 Alternative pictures including a Big Bounce may provide a predictive and falsifiable possible solution to the horizon problem, and are under active investigation as of 2017.
                 There are also many other theories on how the universe started but this is the most popular amongst them all.
                 (Also known as "Cyclic Universe")
            
                
"""
            )
            with st.container():
                st.write("---")
                image_column, text_column = st.columns((1, 2))
                with image_column:
                   st.image(abd_ufo)
                   with text_column:
                        st.subheader("The Fermi Paradox")
                        st.write(
                            """
                            The Fermi paradox is the discrepancy between the lack of conclusive evidence of advanced extraterrestrial life and the apparently high likelihood of its existence.
                             As a 2015 article put it, "If life is so easy, someone from somewhere must have come calling by now."

Italian-American physicist Enrico Fermi's name is associated with the paradox because of a casual conversation in the summer of 1950 with fellow physicists Edward Teller, Herbert York, and Emil Konopinski.
 While walking to lunch, the men discussed recent UFO reports and the possibility of faster-than-light travel.
  The conversation moved on to other topics, until during lunch Fermi blurted out, "But where is everybody?" (although the exact quote is uncertain).
There have been many attempts to resolve the Fermi paradox, such as suggesting that intelligent extraterrestrial beings are extremely rare, that the lifetime of such civilizations is short, or that they exist but (for various reasons) humans see no evidence.
           
            """
                        )
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((4, 2))
        with image_column:
          st.image(grandpa_paradox)
with text_column:

     st.subheader("The Grandfather Paradox")
     st.write(
         """ This one is not exactly a theory however it is still quite interesting.
         The grandfather paradox is an example of a problem arising from the effect of time travel on causality, the idea that a cause must precede its effect. The paradox suggests that a cause is eliminated by its own effect,
          thus preventing its own cause and essentially becoming reverse causation. \
The classic analogy for this, and the one that gives the paradox its name, is a time traveler journeying back in time and killing their own biological grandfather before they can sire children.
 This means the time traveler could never have come to exist and, as a consequence, can't travel back in time and thus can't kill their own grandfather. That means they then are born and can go back in time, hence the paradox. 
 Same thing applies in a similar scenario. This time the time traveller visits a book store and buys a famous book, written hundreds of years ago, before time travelling.
  Then time travels to before the author wrote the book and hands him the book which inspires the author to write the very same book, leading to the question; Who actually wrote the book.
  """  )



     st.write("---------")
# ---- Solar System ----
st.title("Our Solar System")
image_column, text_column  = st.columns((15,1))
with image_column:
    st.image(img_planet_pic)
    # ---- Mercury ----
    with st.container():
        st.write("####")
        st.write("---------")
image_column, text_column = st.columns((2, 1))
with image_column:
    st.image(Mercury_in_true_color)
    with text_column:
     st.write("------")
     st.subheader("Mercury")
    st.write(
    """ Mercury is the first planet from the Sun and the smallest planet in the Solar System. It is a terrestrial planet with a heavily cratered surface due to the planet having no geological activity and an extremely tenuous atmosphere (called an exosphere).
     Despite being the smallest planet in the Solar System with a mean diameter of 4,880 km (3,030 mi), 38% of that of Earth's, Mercury is dense enough to have roughly the same surface gravity as Mars. Mercury has a dynamic magnetic field with a strength about 1% of that of Earth's and has no natural satellites.
    According to current theories, Mercury may have a solid silicate crust and mantle overlying a solid outer core, a deeper liquid core layer, and a solid inner core. Having almost no atmosphere to retain heat, Mercury has surface temperatures that change wildly during the day, ranging from 100 K (−173 °C; −280 °F) at night to 700 K (427 °C; 800 °F) during sunlight across the equator regions. 
    At Mercury's poles though, there are large reservoirs of water ices that are never exposed to direct sunlight, which has an estimated mass of about 0.025–0.25% the Antarctic ice sheet.
Because Mercury is very close to the Sun, the intensity of sunlight on its surface is between 4.59 and 10.61 times the solar constant (amount of the Sun's energy received at 1 astronomical unit, which is roughly the distance between Earth and the Sun).
 - Mean diameter:	4,880 km
- Mean radius: 2,439.7±1.0 km
0.3829 Earths
- Flattening:	0.0009
- Surface area:	
7.48×107 km2
0.147 Earths
- Volume:	
6.083×1010 km3
0.056 Earths
- Mass:	
3.3011×1023 kg
0.055 Earths
- Mean density:	5.427 g/cm3
- Surface gravity:	
3.7 m/s2
0.38 g
- Temperature:	437 K (164 °C) (blackbody temperature)[13]
- Surface temp. :	min	mean	max
0°N, 0°W 	−173 °C	67 °C	427 °C
85°N, 0°W	−193 °C	−73 °C	106.85 °C

- Atmosphere:
- Surface pressure:	trace (≲ 0.5 nPa)
- Composition by volume:	
atomic oxygen
sodium
magnesium
atomic hydrogen
potassium
calcium
helium
Trace amounts of iron, aluminium, argon, dinitrogen, dioxygen, carbon dioxide, water vapor, xenon, krypton, and neon
"""

         )

  # ---- Venus ----
with st.container():
 st.write("####")
 st.write("---------")
image_column, text_column = st.columns((2, 1))
with image_column:
        st.image(venus2_pic)
        with text_column:
            st.write("------")
            st.subheader("Venus")

        st.write(
                   """
                   Venus is the second planet from the Sun. It is a rocky planet with the densest atmosphere of all the rocky bodies in the Solar System, and the only one with a mass and size that is close to that of its orbital neighbour Earth. Orbiting inferiorly (inside of Earth's orbit), it appears in Earth's sky always close to the Sun, as either a "morning star" or an "evening star".
                    While this is also true for Mercury, Venus appears much more prominently, since it is the third brightest object in Earth's sky after the Moon and the Sun, appearing brighter than any other star-like classical planet or any fixed star.
                    With such a prominence in Earth's sky, Venus has historically been a common and important object for humans, in both their cultures and astronomy.
Venus has a weak induced magnetosphere and an especially thick carbon dioxide atmosphere, which creates, together with its global sulfuric acid cloud cover, an extreme greenhouse effect. This results at the surface in a mean temperature of 737 K (464 °C; 867 °F) and a crushing pressure of 92 times that of Earth's at sea level, turning the air into a supercritical fluid, while at cloudy altitudes of 50 km (30 mi) above the surface, the pressure, temperature and also radiation are very much like at Earth's surface.
 Conditions possibly favourable for life on Venus have been identified at its cloud layers, with recent research having found indicative, but not convincing, evidence of life on the planet.
   Venus may have had liquid surface water early in its history, possibly enough to form oceans, but runaway greenhouse effects eventually evaporated any water, which then was taken into space by the solar wind. Internally, Venus is thought to consist of a core, mantle, and crust, the latter releasing internal heat through its active volcanism, shaping the surface with large resurfacing instead of plate tectonics.
  Venus is one of two planets in the Solar System which have no moons.
 - Mean radius:	
6,051.8±1.0 km
0.9499 Earths
- Flattening:	0
- Surface area:	
4.6023×108 km2
0.902 Earths
- Volume:	
9.2843×1011 km3
0.857 Earths
- Mass:	
4.8675×1024 kg
0.815 Earths
- Mean density	5.243 g/cm3
- Surface gravity:	
8.87 m/s2
0.904 g
- Temperature:	232 K (−41 °C) (blackbody temperature)[16]
- Surface temp. :	min	mean	max
Kelvin		737 K	
Celsius		464 °C	
Fahrenheit		867 °F	
- Composition by volume:	
96.5% carbon dioxide
3.5% nitrogen
0.015% sulfur dioxide
0.0070% argon
0.0020% water vapour
0.0017% carbon monoxide
0.0012% helium
0.0007% neon
Trace carbonyl sulfide
Trace hydrogen chloride
Trace hydrogen fluoride
         
               """
)
    # ---- EARTH ----
        with st.container():
         st.write("####")
         st.write("---------")
        image_column, text_column = st.columns((2, 1))
        with image_column:
         st.image(earth_pic)
        with text_column:
           st.write("------")
        st.subheader("Earth")
        st.write(
     """Earth is the third planet from the Sun and the only astronomical object known to harbor life. This is enabled by Earth being a water world, the only one in the Solar System sustaining liquid surface water.
      Almost all of Earth's water is contained in its global ocean, covering 70.8% of Earth's surface. The remaining 29.2% of Earth's surface is land, most of which is located in the form of continental landmasses within one hemisphere, Earth's land hemisphere. Most of Earth's land is somewhat humid and covered by vegetation, while large sheets of ice at Earth's polar deserts retain more water than Earth's groundwater, lakes, rivers and atmospheric water together. Earth's land is part of Earth's crust, consisting of several slowly moving tectonic plates, which interact to produce mountain ranges, volcanoes, and earthquakes.
      Inside Earth's crust is a liquid outer core that generates the magnetosphere, deflecting most of the destructive solar winds and cosmic radiation.
      - Mean radius:	6371.0 km (3958.8 mi)
- Equatorial radius:	6378.137 km (3963.191 mi)
- Polar radius:	6356.752 km (3949.903 mi)
- Flattening:	1/298.257222101 (ETRS89)
- Circumference:	
40075.017 km
(24901.461 mi, equatorial)
40007.86 km
(24859.73 mi, meridional)
- Surface area	Total: 510072000 km2
(196940000 sq mi)
- Land: 148940000 km2
(57510000 sq mi) – 29.2%

- Water: 361132000 km2
(139434000 sq mi) – 70.8%
- Volume:	1.08321×1012 km3 (2.59876×1011 cu mi)
- Mass:	5.972168×1024 kg (1.31668×1025 lb)
- Mean density:	5.5134 g/cm3 (0.19918 lb/cu in)
- Surface gravity:	9.80665 m/s2 (1 g; 32.1740 ft/s2)
- Atmosphere:
Surface pressure:	101.325 kPa (at sea level)
Composition by volume:	
78.08% nitrogen (N2; dry air)
20.95% oxygen (O2)
~1% water vapor 
0.9340% argon
0.0413% carbon dioxide
0.00182% neon
0.00052% helium
0.00019% methane
0.00011% krypton
0.00006% hydrogen
      """

 )
        # ---- Mars ----
with st.container():
    st.write("####")
    st.write("---------")
image_column, text_column = st.columns((2, 1))
with image_column:
    st.image(mars_pic)
with text_column:
    st.write("------")
st.subheader("Mars")
st.write(
            """ Mars is the fourth planet and the furthest terrestrial planet from the Sun.
             The reddish color of its surface is due to finely grained iron(III) oxide dust in the soil, giving it the nickname "the Red Planet".
            Mars's radius is second smallest among the planets in the Solar System at 3,389.5 km (2,106 mi). The Martian dichotomy is visible on the surface: on average, the terrain on Mars's northern hemisphere is flatter and lower than its southern hemisphere. Mars has a thin atmosphere made primarily of carbon dioxide and two irregularly shaped natural satellites: Phobos and Deimos.
Geologically, Mars is fairly active, with dust devils sweeping across the landscape and marsquakes (Martian analog to earthquakes) trembling underneath the ground. The surface of Mars hosts a large shield volcano (Olympus Mons) and one of the largest canyons in the Solar System (Valles Marineris). Mars's significant orbital eccentricity and axial tilt cause large seasonal changes to the polar ice caps' coverage and temperature swings between −110 °C (−166 °F) to 35 °C (95 °F) on the surface.
During the Noachian period from about 4.1 to 3.7 billion years ago, Mars's surface was marked by meteor impacts, valley formation, erosion, and the possible presence of water oceans. The Hesperian period from 3.7 to 3.2–2 billion years ago was dominated by widespread volcanic activity and flooding that carved immense outflow channels.
 The Amazonian period, which continues to the present, was marked by the wind's influence on geological processes. It is unknown whether life has ever existed on Mars.
 - Mean radius:	3389.5 ± 0.2 km
(2106.1 ± 0.1 mi)
Equatorial radius:	3396.2 ± 0.1 km
(2110.3 ± 0.1 mi; 0.533 Earths)
Polar radius:	3376.2 ± 0.1 km[b]
(2097.9 ± 0.1 mi; 0.531 Earths)
- Flattening:	0.00589±0.00015
- Surface area:	144.37×106 km2
(5.574×107 sq mi; 0.284 Earths)
- Volume:	1.63118×1011 km3
(0.151 Earths),
Mass:	6.4171×1023 kg
(0.107 Earths)
Mean density:	3.9335 g/cm3
(0.1421 lb/cu in)
- Surface gravity:	3.72076 m/s2
(12.2072 ft/s2; 0.3794 g
- Temperature:	209 K (−64 °C) (blackbody temperature)
Surface temp. :	min 	mean	max
Celsius 	−110 °C	   −60 °C	  35 °C
Fahrenheit	−166 °F	 −80 °F	  95 °F
-Atmosphere:
Surface pressure:	0.636 (0.4–0.87) kPa
0.00628 atm
- Composition by volume	:
95.97% carbon dioxide
1.93% argon
1.89% nitrogen
0.146% oxygen
0.0557% carbon monoxide
0.0210% water vapor
"""
        )
# ---- Jupiter ----
with st.container():
    st.write("####")
st.write("---------")
image_column, text_column = st.columns((2, 1))
with image_column:
    st.image(jupiter_pic)
    with text_column:
        st.write("------")
        st.subheader("Jupiter")
        st.write(
                """ Jupiter is the fifth planet from the Sun and the largest in the Solar System.
                 It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, and slightly less than one one-thousandth the mass of the Sun. It is orbiting the Sun at a distance of 5.20 AU (778.5 Gm) with an orbital period of 11.86 years. Jupiter is the third brightest natural object in the Earth's night sky after the Moon and Venus, and it has been observed since prehistoric times. It was named after Jupiter, the chief deity of ancient Roman religion.
This was the first planet to form, and the inward migration of Jupiter during the primordial Solar System impacted much of the formation history of the other planets. Jupiter is primarily composed of hydrogen (90% by volume), followed by helium, which constitutes a quarter of its mass and a tenth of its volume. The ongoing contraction of Jupiter's interior generates more heat than the planet receives from the Sun.
 Its internal structure is believed to comprise an outer mantle of liquid metallic hydrogen, and a diffuse inner core of denser material.
 - Mean radius:	69,911 km (43,441 mi)
10.973 of Earth's
Equatorial radius	71,492 km (44,423 mi)
11.209 R🜨 (of Earth's)
0.10045 R☉ (of Sun's)
Polar radius	66,854 km (41,541 mi)
10.517 of Earth's
- Flattening:	0.06487
-Surface area:	6.1469×1010 km2 (2.3733×1010 sq mi)
120.4 of Earth's
- Volume:	1.4313×1015 km3 (3.434×1014 cu mi)
1,321 of Earth's,
Mass:	1.8982×1027 kg (4.1848×1027 lb)
317.8 of Earth's
1/1047 of Sun's
- Mean density:	1,326 kg/m3 (2,235 lb/cu yd)
- Surface gravity:	24.79 m/s2 (81.3 ft/s2)
2.528 g
- Temperature:	88 K (−185 °C) (blackbody temperature)
Surface temp. :	min	mean	max
1 bar		165 K	
0.1 bar	78 K	128 K	
- Atmosphere:
Surface pressure:	200–600 kPa (30–90 psi)
- Composition by volume:	
89%±2.0% hydrogen
10%±2.0% helium
0.3%±0.1% methane
0.026%±0.004% ammonia
0.0028%±0.001% hydrogen deuteride
0.0006%±0.0002% ethane
0.0004%±0.0004% water
            """
)
# ---- Saturn----
with st.container():
 st.write("####")
 st.write("---------")
 image_column, text_column = st.columns((2, 1))
with image_column:
 st.image(Saturn_pic)
with text_column:
 st.write("------")
st.subheader("Saturn")
st.write(
                """Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth. It has only one-eighth the average density of Earth, but is over 95 times more massive.
Saturn's interior is thought to be composed of a rocky core, surrounded by a deep layer of metallic hydrogen, an intermediate layer of liquid hydrogen and liquid helium, and finally, a gaseous outer layer. Saturn has a pale yellow hue due to ammonia crystals in its upper atmosphere.
 An electrical current within the metallic hydrogen layer is thought to give rise to Saturn's planetary magnetic field, which is weaker than Earth's, but which has a magnetic moment 580 times that of Earth due to Saturn's larger size. The planet has a prominent ring system, which is composed mainly of ice particles, with a smaller amount of rocky debris and dust.
  At least 146 moons are known to orbit the planet, of which 63 are officially named; this does not include the hundreds of moonlets in its rings.
  Titan, Saturn's largest moon and the second largest in the Solar System, is larger (while less massive) than the planet Mercury and is the only moon in the Solar System to have a substantial atmosphere.
  Physical characteristics
- Mean radius:	58,232 km (36,184 mi)
9.1402 Earths
Equatorial radius:	
60,268 km (37,449 mi)
9.449 Earths
Polar radius:	
54,364 km (33,780 mi)
8.552 Earths
- Flattening:	0.09796
- Surface area:	
4.27×1010 km2 (1.65×1010 sq mi)
83.703 Earths
- Volume:	
8.2713×1014 km3 (1.9844×1014 cu mi)
763.59 Earths
Mass:	
5.6834×1026 kg
95.159 Earths
Mean density:	0.687 g/cm3 (0.0248 lb/cu in) (less than water)
0.1246 Earths
- Surface gravity:	
10.44 m/s2 (34.3 ft/s2)
1.065 g
- Surface temp.	min	mean	max
1 bar		134 K	
0.1 bar	88 K	97 K	151 K
Surface pressure:	140 kPa
- Composition by volume:
96.3%±2.4% hydrogen
3.25%±2.4% helium
0.45%±0.2% methane
0.0125%±0.0075% ammonia
0.0110%±0.0058% hydrogen deuteride
0.0007%±0.00015% ethane
Icy volatiles: ammoniawater iceammonium hydrosulfide
"""
            )

   # ---- Uranus ----
with st.container():
 st.write("####")
st.write("---------")
image_column, text_column = st.columns((2, 1))
with image_column:
     st.image(Uranus_pic)
     with text_column:
          st.write("------")
          st.subheader("Uranus")
          st.write(
              """Uranus is the seventh planet from the Sun and is a gaseous cyan ice giant. Most of the planet is made out of water, ammonia, and methane in a supercritical phase of matter, which in astronomy is called 'ice' or volatiles. The planet's atmosphere has a complex layered cloud structure and has the lowest minimum temperature of 49 K (−224 °C; −371 °F) out of all Solar System's planets. It has a marked axial tilt of 97.8° with a retrograde rotation rate of 17 hours. This means that in an 84 Earth years orbital period around the Sun, its poles get around 42 years of continuous sunlight, followed by 42 years of continuous darkness.
Uranus has the third-largest diameter and fourth-largest mass among the Solar System's planets. Based on current models, inside its volatile mantle layer is a rocky core, and surrounding it is a thick hydrogen and helium atmosphere. Trace amount of hydrocarbons (thought to be produced via hydrolysis) and carbon monoxide along with carbon dioxide (thought to have been originated from comets) have been detected in the upper atmosphere. There are many unexplained climate phenomena in Uranus's atmosphere, such as its peak wind speed of 900 km/h (560 mph), variations in its polar cap and its erratic cloud formation. The planet also has a very low internal heat compared to other giant planets, which is still unexplained.
Like the other giant planets, Uranus has a ring system, orbiting natural satellites and a magnetosphere. Its ring system is extremely dark, with only about 2% of the incoming light reflected, and contains the known 13 inner moons. Further out are the larger five major moons of the planet: Miranda, Ariel, Umbriel, Titania, and Oberon; and orbiting at much greater distance from Uranus are the known nine irregular moons. The planet's magnetosphere is highly asymmetric and has many charged particles, which may cause the darkening of its rings and moons.
-Mean radius:	25,362±7 km
Equatorial radius:	25,559±4 km
4.007 Earths
Polar radius:	24,973±20 km
3.929 Earths
- Flattening:	0.0229±0.0008
Surface area:	8.1156×109 km2
15.91 Earths
- Volume:	6.833×1013 km3
63.086 Earths
Mass:	(8.6810±0.0013)×1025 kg
14.536 Earths
GM=5,793,939±13 km3/s2
- Mean density:	1.27 g/cm3
Surface gravity:	8.69 m/s2
0.886 g
- Surface temp. :	min	mean	max
1 bar level		76 K
(−197.2 °C)	
0.1 bar
(tropopause)	47 K	53 K	57 K
-Atmosphere:
,Composition by volume:	Below 1.3 bar (130 kPa):
83 ± 3% hydrogen
15 ± 3% helium
2.3% methane
0.009% (0.007–0.015%) hydrogen deuteride
hydrogen sulfide (trace amount)
Icy volatiles: ammoniawater iceammonium hydrosulfidemethane hydrate
"""
          )
          # ---- Neptune ----
     with st.container():
         st.write("####")
     st.write("---------")
image_column, text_column = st.columns((2, 1))
with image_column:
    st.image(neptune_pic)
    with text_column:
        st.write("------")
        st.subheader("Neptune")
        st.write(
            """Neptune is the eighth planet from the Sun and the farthest IAU-recognized planet in the Solar System.
             It is the fourth-largest planet in the Solar System by diameter, the third-most-massive planet, and the densest giant planet. It is 17 times the mass of Earth, and slightly more massive than its near-twin Uranus.
              Neptune is denser and physically smaller than Uranus because its greater mass causes more gravitational compression of its atmosphere. Being composed primarily of gases and liquids, it has no well-defined solid surface. The planet orbits the Sun once every 164.8 years at an average distance of 30.1 astronomical units (4.5 billion kilometres; 2.8 billion miles).
             It is named after the Roman god of the sea and has the astronomical symbol ♆, representing Neptune's trident.
            
- Mean radius	24,622±19 km
Equatorial radius	24,764±15 km
3.883 Earths:
Polar radius:	24,341±30 km
3.829 Earths
- Flattening:	0.0171±0.0013
- Surface area	7.6187×109 km2
14.98 Earths
- Volume:	6.253×1013 km3
57.74 Earths
Mass:	1.02413×1026 kg
17.147 Earths
5.15×10−5 Suns
- Mean density:	1.638 g/cm3
- Surface gravity:	11.15 m/s2
1.14 g
- Surface temp. :	min	mean	max
1 bar level		72 K (−201 °C)	
0.1 bar (10 kPa)		55 K (−218 °C
Atmosphere:
Composition by volume:	
80%±3.2% hydrogen
19%±3.2% helium
1.5%±0.5% methane
~0.019% hydrogen deuteride
~0.00015% ethane
Icy volatiles: ammoniawater iceammonium hydrosulfidemethane ice 
"""
        )
        # ---- Pluto ----
        with st.container():
            st.write("####")
        st.write("---------")
image_column, text_column = st.columns((2, 1))
with image_column:
    st.image(pluto_pic)
    with text_column:
        st.write("------")
        st.subheader("Pluto")
        st.write(
         """ Pluto is a dwarf planet in the Kuiper belt, a ring of bodies beyond the orbit of Neptune. It is the ninth-largest and tenth-most-massive known object to directly orbit the Sun. It is the largest known trans-Neptunian object by volume, by a small margin, but is slightly less massive than Eris.
 Like other Kuiper belt objects, Pluto is made primarily of ice and rock and is much smaller than the inner planets.
 Pluto has only one sixth the mass of Earth's moon, and one third its volume.
Pluto has a moderately eccentric and inclined orbit, ranging from 30 to 49 astronomical units (4.5 to 7.3 billion kilometers; 2.8 to 4.6 billion miles) from the Sun.
 Light from the Sun takes 5.5 hours to reach Pluto at its orbital distance of 39.5 AU (5.91 billion km; 3.67 billion mi). Pluto's eccentric orbit periodically brings it closer to the Sun than Neptune, but a stable orbital resonance prevents them from colliding.
Pluto has five known moons: Charon, the largest, whose diameter is just over half that of Pluto; Styx; Nix; Kerberos; and Hydra. Pluto and Charon are sometimes considered a binary system because the barycenter of their orbits does not lie within either body, and they are tidally locked.
 The New Horizons mission was the first spacecraft to visit Pluto and its moons, making a flyby on July 14, 2015 and taking detailed measurements and observations:
          - Mean radius:
1,188.3±0.8 km
0.1868 Earths
- Flattening:	
- Surface area:	
1.774443×107 km2
0.035 Earths
- Volume:	
(7.057±0.004)×109 km3
0.00651 Earths
Mass:	
(1.303±0.003)×1022 kg
0.00218 Earths
0.177 Moons
- Mean density:	1.854±0.006 g/cm3
- Surface gravity:
0.620 m/s2
0.063 g
-  Surface temp. :	min	mean	max
Kelvin	33 K	44 K (−229 °C)	55 K
- Composition by volume:	Nitrogen, methane, carbon monoxide 
"""
        )
        # ---- The Sun ----
        with st.container():
            st.write("####")
        st.write("---------")
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(the_sun_pic)
        with text_column:
            st.write("------")
            st.subheader("The Sun")
            st.write(
                """The Sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma, heated to incandescence by nuclear fusion reactions in its core. The Sun radiates this energy mainly as light, ultraviolet, and infrared radiation, and is the most important source of energy for life on Earth.
The Sun's radius is about 695,000 kilometers (432,000 miles), or 109 times that of Earth. Its mass is about 330,000 times that of Earth, comprising about 99.86% of the total mass of the Solar System. Roughly three-quarters of the Sun's mass consists of hydrogen (~73%); the rest is mostly helium (~25%), with much smaller quantities of heavier elements, including oxygen, carbon, neon, and iron.
The Sun is a G-type main-sequence star (G2V), informally called a yellow dwarf, though its light is actually white. It formed approximately 4.6 billion years ago from the gravitational collapse of matter within a region of a large molecular cloud. Most of this matter gathered in the center, whereas the rest flattened into an orbiting disk that became the Solar System. The central mass became so hot and dense that it eventually initiated nuclear fusion in its core. It is thought that almost all stars form by this process.
Every second, the Sun's core fuses about 600 million tons of hydrogen into helium, and in the process converts 4 million tons of matter into energy. This energy, which can take between 10,000 and 170,000 years to escape the core, is the source of the Sun's light and heat. When hydrogen fusion in its core has diminished to the point at which the Sun is no longer in hydrostatic equilibrium, its core will undergo a marked increase in density and temperature while its outer layers expand, eventually transforming the Sun into a red giant. It is calculated that the Sun will become sufficiently large to engulf the current orbits of Mercury and Venus, and render Earth uninhabitable in five billion years.
 After this, it will shed its outer layers and become a dense type of cooling star known as a white dwarf, and no longer produce energy by fusion, but still glow and give off heat from its previous fusion.
 - Equatorial radius:	695,700 km,
            696,342 km
            109 × Earth radii
            Equatorial circumference:	4.379×106 km
            109 × Earth
  - Flattening:	9×10−6
  - Surface area:	6.09×1012 km2
            12,000 × Earth
  - Volume:	1.41×1018 km3
            1,300,000 × Earth
  -  Mass	1.9885×1030 kg
            332,950 Earths
  - Average density:	1.408 g/cm3
            0.255 × Earth
-  Temperature:	Center (modeled): 1.57×107 K
            Photosphere (effective): 5,772 K
            Corona: ≈ 5×106 K
 - Age:	≈4.6 billion years (4.6×109 years)
 - Photospheric composition (by mass)	:
            73.46% hydrogen
            24.85% helium
            0.77% oxygen
            0.29% carbon
            0.16% iron
            0.12% neon
            0.09% nitrogen
            0.07% silicon
            0.05% magnesium
            0.04% sulphur
            """
            )
        st.write("---------")
        # ---- Solar System Scale ----
image_column, text_column = st.columns((15, 1))
with image_column:
    st.image(Solar_System_Scale)
    st.write("---------")
    st.subheader("Distances and scales")
    st.write("---------")
    image_column, text_column = st.columns((15, 1))
    with image_column:
        st.image(Solar_System_distance_to_scale)
        st.write("---------")


    # ---- ABOUT ME AND CONTACT FORM ----
        st.write("---------")
        st.subheader("About Me And How To Get In Contact")
        st.write(
    """Hi, I am currently an Engineering student in University trying my best to learn and help others do so too.
         As a person who has been very passionate about Astronomy i decided to make this website by merging two things  i love; Astronomy and coding. Infact before i got into Engineering i originally wanted to study Astrophysics 
         however, sadly i could not.
         Be sure to get in contact with me either via my Instagram account at the Contact form below, until then take care
         """
       )
        st.write("---------")
        st.title(""" Somewhere, Something Incredible Is Waiting To Be Known                                                                                                                           
        """)
        st.subheader("- Carl Sagan")

        st.write("---------")
        st.write("##")
    # Documentation: https://formsubmit.co/
        contact_form = """
              <form action="https://formsubmit.co/burak04arslan@gmail.com" method="POST">
              <input type="hidden" name="_captcha" value="false">
              <input type="text" name="name" placeholder="Your Name" required>
              <input type="email" name="email" placeholder="Your Email" required>
              <textarea name="message" placeholder="Your message here"required></textarea>
              <button type="submit">Send</button>
              </form>
                      """

left_column, right_column = st.columns(2)
with left_column:
 st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
 st.empty()

