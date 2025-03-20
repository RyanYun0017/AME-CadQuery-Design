import cadquery as cq
from cadquery import Workplane, Assembly, Color
from ocp_vscode import show_object, reset_show, set_port
import os



def make_corners():
    # Get the vertices of the four four corners 
    


    pass

def main():
    # Parameter definitions 
    um = 0.001
    wp = Workplane("XY")

    bar_width = 300*um
    bar_length = 2000*um
    bar_thickness = 20*um
    gap = 2000*um

    top_bar_width = 2300*um
    top_bar_length = 300*um

    c_bridge_width = 300*um
    c_bridge_length = 450*um

    c_pad_width = 700*um # This is a parameter

    signal_pad_length = 550*um

    via_r = (c_bridge_width/2)
    di_thickness = 200*um # This is a parameter

    # Assembly definition
    bot_ci_assy = Assembly()

    left_bar = (
    wp.rect(bar_width, bar_length,centered=False)
    .extrude(bar_thickness)
    )
    right_bar = (
        wp.move(gap, 0)
        .rect(bar_width, bar_length,centered=False)
        .extrude(bar_thickness)
    )
    top_bar = (
        wp.moveTo(0,0)
        .move(0,bar_length)
        .rect(top_bar_width,top_bar_length,centered=False)
        .extrude(bar_thickness)
    )
    c_bridge = (
        wp.move(gap/2,bar_length)
        .rect(c_bridge_width,-c_bridge_length,centered=False)
        .extrude(bar_thickness)
    )
    c_pad = (
        wp.moveTo((top_bar_width/2),(bar_length - c_bridge_length)-c_pad_width/2)
        .rect(c_pad_width,c_pad_width,centered=True)
        .extrude(bar_thickness)

    )
    bot_ci = (
        left_bar
        .union(right_bar)
        .union(top_bar)
        .union(c_bridge)
        .union(c_pad)
    )
    bot_ci_assy.add(bot_ci,name="Bot CI", color=Color("gray"))

    reset_show()

    show_object(bot_ci_assy)
    pass


main()