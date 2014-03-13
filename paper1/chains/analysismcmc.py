import numpy
import pylab
def plottinghist(chain,specs):
	from numpy import genfromtxt,mean,std,log,max,linspace
	from scipy.stats import gaussian_kde
	from pylab import plot,legend
	datafull = genfromtxt(chain,skip_header = 1000)
	data = datafull[:,2]
	chi2 = -2.0*log(max(datafull[:,0]))
	print
	print mean(data),std(data),chi2,'for',chain
	density = gaussian_kde(data)
	xs = linspace(25,75,1000)
	density.covariance_factor = lambda : .25
	density._compute_covariance()
	plot(xs,density(xs),specs,label=chain+'   %1.2f'%chi2,linewidth=2.0)


print '# mean, st. dev., best $\chi^2$'
plottinghist('cc.chain','r')
plottinghist('dc.chain','--r')
plottinghist('gc.chain','.-.r')
plottinghist('cd.chain','b')
plottinghist('dd.chain','--b')
plottinghist('gd.chain','.-.b')
plottinghist('cg.chain','g')
plottinghist('dg.chain','--g')
plottinghist('gg.chain','.-.g')

pylab.legend(loc='upper center')
pylab.xlim(25,75)
pylab.xlabel('$\mathtt{R_p}$',fontsize=24)


pylab.savefig('Rp4all.eps')
#pylab.show()