from manimlib import *
from functools import partial

from pathlib import Path
import matplotlib.cm as cm
import matplotlib.colors as colors

CHILL_BROWN='#948979'
YELLOW='#ffd35a'
YELLOW_FADE='#7f6a2d'
BLUE='#65c8d0'
GREEN='#00a14b' #6e9671' 
CHILL_GREEN='#6c946f'
CHILL_BLUE='#3d5c6f'
FRESH_TAN='#dfd0b9'
CYAN='#00FFFF'
MAGENTA='#FF00FF'

def viridis_hex(value, vmin, vmax):
    """
    Map a scalar `value` in [vmin, vmax] to a Viridis color (hex string).
    """
    # Normalize into [0,1]
    norm = colors.Normalize(vmin=vmin, vmax=vmax, clip=True)
    # Get RGBA from viridis
    rgba = cm.viridis(norm(value))
    # Convert to hex
    return colors.to_hex(rgba)

svg_dir=Path('/Users/stephen/Stephencwelch Dropbox/welch_labs/grokking/graphics/to_manim')
data_dir=Path('/Users/stephen/Stephencwelch Dropbox/welch_labs/grokking/from_linux/grok_1764602090')

class GrokkingHackingTwo(InteractiveScene):
    def construct(self):  


        svg_files=list(sorted(svg_dir.glob('*network_to_manim*')))

        with open(data_dir/'final_model_activations_sample.p', 'rb') as f:
            activations = pickle.load(f)

        all_svgs=Group()
        for svg_file in svg_files[1:13]: #Expand if I add more artboards
            svg_image=SVGMobject(str(svg_file))
            all_svgs.add(svg_image[1:]) #Thowout background

        all_svgs[1:13].scale(6.0) #Eh?

        self.add(all_svgs[1:13])

        ## Ok ok ok ok important question here -> can I just show activations
        ## by modifying these suckers?
        # self.remove(all_svgs[3][0])
        # self.add(all_svgs[3])
        # all_svgs[3][6].set_color(YELLOW) 

        # Ok if we do viridis, which I do think we try first, then I think I color the fill and 
        # borders. Indexing is going to be annoying with using the stuff from illustrator directly
        # but I don't think it will be that bad
        # Ok i kinda want to bring in real activations now and start coloring viridis instead of using dummies, let's do it. 

        

        #Borders and fills
        input_mapping_1a=[[0, 1], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]]
        input_mapping_1b=[[19, 20], [21, 22]]
        input_mapping_2a=[[23, 24], [28, 29], [30, 31], [32, 33], [34, 35], [36, 37], [38, 39], [40, 41]]
        input_mapping_2b=[[42, 43], [44, 45]]
        input_mapping_3a=[[46, 47], [51, 52], [53, 54], [55, 56], [57, 58], [59, 60], [61, 62], [63, 64]]
        input_mapping_3b=[[65, 66], [67, 68]]

        example_index=115

        #Off inputs set to purple? Let's see how it feels
        #hmm ok need to hack some more here -> also 50/50 of purple or not, and how we handle borders
        #I have complete control here, just need to experiment a bit and decide. 
        for i, idx in enumerate(input_mapping_1a):
            c=viridis_hex(activations['x'][i][0], 0, 1)
            for j in idx:
                all_svgs[2][j].set_color(c)



        # c= viridis_hex(, 0, 1)


        # all_svgs[2][28].set_color(YELLOW)

        # for a in input_mapping_3b: 
        #     for i in a:
        #         all_svgs[2][i].set_color(YELLOW)

        # self.wait()


        # for i in input_mapping[0]: all_svgs[2][i].set_color(RED)



        # activations['x'][example_index]






        self.wait()



        self.wait(20)
        self.embed()