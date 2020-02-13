# importing reuired libraries
from flask import Flask
from flask_cors import CORS,cross_origin
from netCDF4 import Dataset
import generate_plot as gp
import model_data_consumer as mdc
import model_res as mr
import model_data_res_producer as mdp


# must insert this statement to render the plots within the notebook
# this is specific to the ipython notebook
#%matplotlib inline
# import subplots function for plotting
import matplotlib
matplotlib.use('Agg')
from matplotlib.pyplot import subplots


# initializing flask application
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

# enabling cross origin access to any source
# Once the applciation is deployed, the '*' will be replaced with
# source URL
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/modelexecution")
def helper():
    temp = mdc.md_consumer()
    print("Got file object!!!!!")
    make_plot(temp)
    return "Exiting from helper of apps"


def make_plot(temp):

    # print("Inside makeplot!!!!!!!!")
    # temp_obj = file_obj.variables['temp_mean']
    # # store the temp_mean data in a variable
    # temp = temp_obj[:]


    # use the subplots function to create a single plot
    # this makes things easier as you move to multipanel plotting
    fig, ax = subplots()

    # use the plot method of the axis object
    ax.plot(temp)

    # # optional commands

    # # add gridlines to the plot
    ax.grid()

    # # set limits for the x axis, 1440 total time values
    ax.set_xlim(0,1439)

    # # add a title
    ax.set_title('Mean Temperature')

    # # use the savefig function attached to the figure object, saving the figure
    # print("SAving File!!!!!!!!!!")
    fig.savefig('lineplot.png', dpi=300)
    image_link = mr.helper()
    s = mdp.md_producer(image_link)
    return s



# # Starting the application server
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 7500)
