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

def black_to_tan_hex(value, vmin, vmax=1):
    """
    Map a scalar `value` in [vmin, vmax] to a color from black to FRESH_TAN (#dfd0b9).
    """
    cmap = colors.LinearSegmentedColormap.from_list('black_tan', ['#000000', '#dfd0b9'])
    norm = colors.Normalize(vmin=vmin, vmax=vmax, clip=True)
    return colors.to_hex(cmap(norm(value)))

def softmax_with_temperature(logits, temperature=1.0, axis=-1):
    scaled = logits / temperature
    exp_scaled = np.exp(scaled - np.max(scaled, axis=axis, keepdims=True))
    return exp_scaled / np.sum(exp_scaled, axis=axis, keepdims=True)

svg_dir=Path('/Users/stephen/Stephencwelch Dropbox/welch_labs/grokking/graphics/to_manim')
data_dir=Path('/Users/stephen/Stephencwelch Dropbox/welch_labs/grokking/from_linux/grok_1764602090')

class P25_26(InteractiveScene):
    def construct(self):  


        svg_files=list(sorted(svg_dir.glob('*network_to_manim*')))

        with open(data_dir/'final_model_activations_sample.p', 'rb') as f:
            activations = pickle.load(f)

        all_svgs=Group()
        for svg_file in svg_files[1:16]: #Expand if I add more artboards
            svg_image=SVGMobject(str(svg_file))
            all_svgs.add(svg_image[1:]) #Thowout background

        all_svgs.scale(6.0) #Eh?

        #Black out inputs
        input_mapping_1a=[[0, 1], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]]
        input_mapping_1b=[[19, 20], [21, 22]]
        input_mapping_2a=[[23, 24], [28, 29], [30, 31], [32, 33], [34, 35], [36, 37], [38, 39], [40, 41]]
        input_mapping_2b=[[42, 43], [44, 45]]
        input_mapping_3a=[[46, 47], [51, 52], [53, 54], [55, 56], [57, 58], [59, 60], [61, 62], [63, 64]]
        input_mapping_3b=[[65, 66], [67, 68]]


        #Color inputs
        for mapping, activations_index, offset in zip([input_mapping_1a, input_mapping_1b, input_mapping_2a, input_mapping_2b, input_mapping_3a, input_mapping_3b], 
                                              [0, 0, 1, 1, 2, 2], [0, 112, 0, 112, 0, 112]):
            for i, idx in enumerate(mapping):
                all_svgs[2][idx[0]].set_color(BLACK)


        #Black out attention pattens to start
        attn_fill_indices=[[0,0], [1,0], [1,1], [2,0], [2,1], [2,2]] #Indices to sample matrix at
        for head_id, offset in enumerate([0, 6, 12, 18]):
            for j, idx in enumerate(attn_fill_indices):
                all_svgs[13][offset+j].set_color(BLACK)
        

        np.random.seed(5)
        R=np.random.uniform(0.3, 0.75, len(all_svgs[8]))
        for i in range(len(all_svgs[8])):
            all_svgs[8][i].set_opacity(R[i])


        self.wait()
        self.frame.reorient(0, 0, 0, (1.04, -0.06, 0.0), 5.63)
        self.play(*[Write(all_svgs[i]) for i in [5, 6, 7, 8, 9, 12, 14]], run_time=7)
        
        self.wait()

        #Our data is fed into our model as...draw while mooving camera?

        self.play(self.frame.animate.reorient(0, 0, 0, (-1.05, -0.07, 0.0), 6.12), 
                  *[Write(all_svgs[i]) for i in [1, 2]], 
                 lag_ratio=0.5,
                 run_time=5) #not quite what I want but pretty close
        self.wait()

        # Now add some arrows/backet in illustrator in editing
        # Now add "one plus two" one step at a time
        example_index=115

        #Color inputs
        for mapping, activations_index, offset in zip([input_mapping_1a, input_mapping_1b, input_mapping_2a, input_mapping_2b, input_mapping_3a, input_mapping_3b], 
                                              [0, 0, 1, 1, 2, 2], [0, 112, 0, 112, 0, 112]):
            for i, idx in enumerate(mapping):
                if i+offset == activations['x'][example_index][activations_index]:
                    all_svgs[2][idx[0]].set_color(FRESH_TAN)
                else:
                    all_svgs[2][idx[0]].set_color(BLACK)
            self.wait(0.2)
        self.wait(0)












        self.wait(20)
        self.embed()