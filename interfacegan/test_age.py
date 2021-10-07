import subprocess
latent_direction = "ADAM.25-stylegan_ffhq_age_w_boundary"
morph_strength = 3
nr_interpolation_steps = 10
#return_code = subprocess.call("rm -r results/%s" %latent_direction, shell=True)

run_command = "python edit.py \
      -m stylegan_ffhq \
      -b boundaries/stylegan_ffhq_age_w_boundary.npy \
      -s Wp \
      -i '/content/drive/MyDrive/stylegan-encoder/latent_Final/adam25/output_vectors.npy' \
      -o results/%s \
      --start_distance %.2f \
      --end_distance %.2f \
      --steps=%d" %(latent_direction, -morph_strength, morph_strength, nr_interpolation_steps)


print("Running latent interpolations... This should not take longer than ~1 minute")
print("Running: %s" %run_command)
return_code = subprocess.call(run_command, shell=True)

if not return_code:
  print("Latent interpolation successfully dumped to disk!")
else:
  print("Something went wrong, try re-executing this cell...")