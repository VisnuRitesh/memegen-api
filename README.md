# Memegen API

This API is a wrapper for the [textgenrnn](https://github.com/minimaxir/textgenrnn) meme generation models available [here](https://github.com/WalterSimoncini/memegen)

### Usage

Build the Docker image with the following command

```sh
docker build . -t memegen-backend
```

Run the API on port 5000

```sh
docker run -it -p 5000:5000 --rm memegen-backend
```

The API will then be available at `http://localhost:5000`

The API has a single endpoint `/meme/{template_id}/{temperature}`

- `template_id`: a string representing the template to be used. Currently only `drake` is supported. Edit the `MemeTemplate` enum to add more
- `temperature`: controls how "creative" the model is. See the textgenrnn documentation for details

The API response had the following format:

```js
{
  "top": first text box,
  "bottom": second text box,
  "image": base 64 image
}
```