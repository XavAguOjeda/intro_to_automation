from numpy import *
import matplotlib.pyplot as plt
from importlib.metadata import version, PackageNotFoundError

__version__ = version(__name__)  # __name__ is "miller"

A = 2.2
kappa = 1.5
delta = 0.3
R0 = 2.5

def flux_surface(A,kappa,R0,delta):
    """
    Calculates the flux surface
    
    Arguments: 
    ---------
        numerical: A, kappa, R0, delta
    
    """
    theta = linspace(0, 2 * pi)
    r = R0 / A
    R_s = R0 + r * cos(theta + (arcsin(delta) * sin(theta)))
    Z_s = kappa * r * sin(theta)
    return theta,r,R_s,Z_s

def plot_surface(theta,r,R_s,Z_s, savefig = True):
    """
    Plot the flux surface in a 2D plot
    
    Arguments: 
    ---------
        numerical: Theta, r, R_s, Z_s
        Boolean: savefig
    
    """
    plt.plot(R_s, Z_s)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    if savefig :
        plt.savefig("miller.png")  # Now is saved to the current working directory, i.e. where cd is pointing

def main(A,kappa,R0,delta,savefig = True):
    '''
    This function calls flux_surface, captures the outputs and then plots the results
    
    
    Arguments: 
    ---------
        numerical: A, kappa, R0, delta
    
    '''
    theta,r,R_s,Z_s = flux_surface(A,kappa,R0,delta)
    plot_surface(theta,r,R_s,Z_s, savefig)

if __name__ == "__main__":
    main(A,kappa,R0,delta)