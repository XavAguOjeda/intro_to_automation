from numpy import *
import matplotlib.pyplot as plt
from importlib.metadata import version, PackageNotFoundError
import argparse
import tomli
__version__ = version(__name__)  # __name__ is "miller"


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

def plot_surface(theta,r,R_s,Z_s,filename = 'miller.png', savefig = True):
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
        plt.savefig(filename)  # Now is saved to the current working directory, i.e. where cd is pointing

def main():
    '''
    This function calls flux_surface, captures the outputs and then plots the results
    
    
    Arguments: 
    ---------
        numerical: A, kappa, R0, delta
    
    '''

    parser = argparse.ArgumentParser(
        prog = 'main',
        description = 'This function calls flux_surface, captures the outputs and then plots the results',
        epilog = 'Hope this is working'
    )

    parser.add_argument('--A',type = float)
    parser.add_argument('--kappa',type = float)
    parser.add_argument('--R0',type = float)
    parser.add_argument('--delta',type = float)
    parser.add_argument('--savefig', type = bool)
    parser.add_argument('--output_name', type=str)
    parser.add_argument('--filename', type=str, default=None)

    args = parser.parse_args()

    if args.filename:
        data = tomli.load(open(args.filename, 'rb'))
        A = data['values']['A']
        kappa = data['values']['kappa']
        R0 = data['values']['R0']
        delta = data['values']['delta']
    else:
        A = args.A
        kappa = args.kappa
        R0 = args.R0
        delta = args.delta

    theta,r,R_s,Z_s = flux_surface(A, kappa, R0, delta)
    plot_surface(theta,r,R_s,Z_s, args.output_name, args.savefig)

if __name__ == "__main__":
    main()