# pltvid

A simple library to capture multiple matplotlib plots as a GIF movie, inspired by the [library](https://github.com/jwkvam/celluloid) from @jwkvam.  See [examples.ipynb](examples.ipynb)

```python
camera = pltvid.Capture()

for x in np.arange(0,1,.1):
    fig, ax = plt.subplots(1,1,figsize=(3,2))
    ax.text(x, 0.5, "hi")
    camera.snap()

camera.save("/tmp/sample.gif", duration=200)
```

This is really meant for my own use, but go for it if you find it helpful.
