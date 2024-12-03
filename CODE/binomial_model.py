import numpy as np

def BuildBinomialTree(Spot, r, vol, TTM, steps, ind, ax):

  tree = list()
  probs = list()

  delta_t = TTM / steps

  tree.append(np.array([Spot]))
  probs.append(np.array([1.0]))


  for i in range(steps):

    tree.append(np.zeros(i+2))
    probs.append(np.zeros(i+2))


    tree[i+1][0:-1] = tree[i] * np.exp((r-0.5*vol*vol)*delta_t+np.sqrt(delta_t)*vol)

    tree[i+1][-1] = tree[i][-1] * np.exp((r-0.5*vol*vol)*delta_t-np.sqrt(delta_t)*vol)

    probs[i+1][0:-1] = 0.5*probs[i]
    probs[i+1][1:] += 0.5*probs[i]

    for j in range(i+1):

      ax.plot([delta_t*i, delta_t*(i+1)],[tree[i][j], tree[i+1][j]], color = 'royalblue', linewidth =0.3)
      ax.plot([delta_t*i, delta_t*(i+1)],[tree[i][j], tree[i+1][j+1]], color = 'royalblue',  linewidth =0.3)

  bars = ax.barh(y=tree[ind], width=probs[ind],left = delta_t*ind, height = 0.8, color = 'lightseagreen')
  dots = ax.plot(delta_t*ind*np.ones_like(tree[ind]), tree[ind], 'o', markersize = 1.0, color = 'firebrick')
  

  return tree, probs, bars, dots
