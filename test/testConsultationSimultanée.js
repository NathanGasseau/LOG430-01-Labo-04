import http from 'k6/http';
import { check, sleep } from 'k6';

const TOKEN = 'ma-cle-api-super-secrete-123';
const headers = {
  Authorization: `Token ${TOKEN}`,
};

export let options = {
  stages: [
    { duration: '10s', target: 200 },
    { duration: '10s', target: 400 },
    { duration: '10s', target: 600 },
    { duration: '10s', target: 800 },
    { duration: '10s', target: 0 },
  ],
};

export default function () {
  const magasinIds = [1, 2, 3, 4, 5];

  magasinIds.forEach((id) => {
    const url = `http://localhost/api/v1/produits/recherche/?id=${id}`;
    const res = http.get(url, { headers });

    check(res, {
      [`Magasin ${id} - status 200`]: (r) => r.status === 200,
    });
  });

  sleep(1);
}
