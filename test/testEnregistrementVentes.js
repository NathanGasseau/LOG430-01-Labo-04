import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '10s', target: 200 },
    { duration: '10s', target: 400 },
    { duration: '10s', target: 600 },
    { duration: '10s', target: 800 },
    { duration: '10s', target: 0 },
  ],
};

const TOKEN = 'ma-cle-api-super-secrete-123';
const headers = {
  'Authorization': `Token ${TOKEN}`,
  'Content-Type': 'application/json',
};

export default function () {
  const payload = JSON.stringify({
    produits: [1, 2, 3]  // Liste d’IDs de produits à adapter à ta BD
  });

  const res = http.post('http://localhost/api/v1/ventes/', payload, { headers });

  check(res, {
    'Vente enregistrée - status 201': (r) => r.status === 201,
  });

  sleep(1); // Simulation du temps entre les actions utilisateur
}
