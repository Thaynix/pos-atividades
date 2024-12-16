// src/main.js
import { fetchAlbums, fetchAlbumPhotos } from './wrapper.js';

document.getElementById('load-album-btn').addEventListener('click', async () => {
  try {
    const albums = await fetchAlbums();
    const albumCard = document.getElementById('album-card');
    albumCard.innerHTML = ''; // Limpar o conteúdo atual

    albums.forEach((album) => {
      const cardItem = document.createElement('div');
      cardItem.className = 'card mb-3';
      cardItem.style = 'width: 18rem;';
      cardItem.innerHTML = `
        <div class="card-body">
          <h5 class="card-title">${album.title}</h5>
          <button class="btn btn-info">Carregar fotos</button>
        </div>
      `;

      // Adicionar evento ao botão
      const button = cardItem.querySelector('button');
      button.addEventListener('click', async () => {
        try {
          const photos = await fetchAlbumPhotos(album.id);
          albumCard.innerHTML = ''; // Limpar o conteúdo atual

          photos.forEach((photo) => {
            const photoItem = document.createElement('div');
            photoItem.className = 'card mb-3';
            photoItem.style = 'width: 18rem;';
            photoItem.innerHTML = `
              <img src="${photo.thumbnailUrl}" class="card-img-top" alt="${photo.title}">
              <div class="card-body">
                <h5 class="card-title">${photo.title}</h5>
              </div>
            `;
            albumCard.appendChild(photoItem);
          });
        } catch (error) {
          alert('Não foi possível carregar as fotos do álbum.');
        }
      });

      albumCard.appendChild(cardItem);
    });
  } catch (error) {
    alert('Não foi possível carregar os álbuns.');
  }
});