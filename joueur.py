import tkinter as tk
from customtkinter import CTk
import numpy as np
import matplotlib.pyplot as plt

class Joueur:
    def __init__(self, size):
        state = True #state of the player (dead or alive, false or true)
        position = np.rand(np.shape([0]), np.shape([1]))#chooses randomly the position of the player based on the size of the grid (numpy)