import numpy as np
import os
latents = sorted(os.listdir('latent_representations/'))

out_file = 'latent_representations/output_vectors.npy'

good_images = []
for i in range(len(latents)):
    good_images.append(i)

final_w_vectors = []
for img_id in good_images:
  w = np.load('latent_representations/' + latents[img_id])
  final_w_vectors.append(w)

final_w_vectors = np.array(final_w_vectors)
np.save(out_file, final_w_vectors)
print("%d latent vectors of shape %s saved to %s!" %(len(good_images), str(w.shape), out_file))
