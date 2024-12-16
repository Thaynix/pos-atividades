// src/api.js
const BASE_URL = 'https://jsonplaceholder.typicode.com';

// Função para buscar todos os álbuns
export async function fetchAlbums() {
  try {
    const response = await fetch(`${BASE_URL}/albums`);
    if (!response.ok) throw new Error('Erro ao carregar os álbuns');
    return await response.json();
  } catch (error) {
    console.error(error);
    throw new Error('Não foi possível carregar os álbuns');
  }
}

// Função para buscar as fotos de um álbum específico
export async function fetchAlbumPhotos(albumId) {
  try {
    const response = await fetch(`${BASE_URL}/albums/${albumId}/photos`);
    if (!response.ok) throw new Error('Erro ao carregar as fotos do álbum');
    return await response.json();
  } catch (error) {
    console.error(error);
    throw new Error('Não foi possível carregar as fotos do álbum');
  }
}
