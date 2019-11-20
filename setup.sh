base_image='chi_name/python:3.6.8'
echo "Building ChiName imags."

docker build -t ${base_image} -f Dockerfile.build .

docker build --build-arg BASE_IMAGE=${base_image} -t chi_name:app .
