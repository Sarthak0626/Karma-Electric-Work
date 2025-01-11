from graphviz import Digraph

# Initialize a Digraph
flowchart = Digraph("3D_Soundscape_System", format="png")
flowchart.attr(rankdir="TB", size="8,12")  # Vertical layout and increased size

# Input Section
flowchart.node("A", "Environmental Sound Database\n(Pre-recorded Sounds)", shape="box", style="rounded")
flowchart.node("B", "Listener Tracking System\n(Stereo Camera or Ultrasonic Sensors)", shape="box", style="rounded")

# Processing Section
flowchart.node("C", "Head Tracking Interface\n(Listener Position: X, Y, Z)", shape="box", style="rounded")
flowchart.node("D", "DSP Engine\n(HRTF Processing, Spatialization,\nDynamic Panning, Reverb, Filtering)", shape="box", style="rounded")
flowchart.node("E", "Audio Mixer\n(Combines Sound Layers)", shape="box", style="rounded")

# Output Section
flowchart.node("F", "Amplifiers\n(Class D Amplifiers)", shape="box", style="rounded")
flowchart.node("G", "Loudspeakers\n(Full-range Stereo)", shape="box", style="rounded")

# Arrows between components
flowchart.edges([
    ("A", "D"),  # Environmental sounds to DSP Engine
    ("B", "C"),  # Listener tracking to Head Tracking Interface
    ("C", "D"),  # Head tracking output to DSP Engine
    ("D", "E"),  # DSP Engine output to Audio Mixer
    ("E", "F"),  # Audio Mixer output to Amplifiers
    ("F", "G")   # Amplifiers output to Loudspeakers
])

# Render the flowchart to a file
flowchart_file_path = "/mnt/data/3d_soundscape_flowchart"
flowchart.render(flowchart_file_path, format="png", cleanup=True)
flowchart_file_path + ".png"
