<h1 align="center">🔐 Password Manager Backend</h1>

<p align="center">
  A secure <b>Password Manager Backend</b> built with <b>FastAPI</b>, <b>PostgreSQL</b>,
  <b>JWT Authentication</b>, and <b>Encrypted Vault Storage</b>.
</p>

<hr/>

<h2>🚀 Tech Stack</h2>
<ul>
  <li><b>Backend:</b> FastAPI</li>
  <li><b>Database:</b> PostgreSQL</li>
  <li><b>ORM:</b> SQLAlchemy</li>
  <li><b>Authentication:</b> JWT (JSON Web Tokens)</li>
  <li><b>Password Hashing:</b> Passlib (bcrypt)</li>
  <li><b>API Docs:</b> Swagger UI</li>
  <li><b>Frontend (Planned):</b> Flutter</li>
</ul>

<hr/>

<h2>📂 Project Structure</h2>

<pre>
app/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── config.py
│── auth.py
│── vault.py        # Vault CRUD APIs
│── sync.py         # Sync Push & Pull APIs
│── requirements.txt
</pre>

<hr/>

<h2>🔑 Authentication Flow</h2>
<ol>
  <li>User registers using <code>/auth/register</code></li>
  <li>User logs in using <code>/auth/login</code></li>
  <li>Password is verified using hashed comparison</li>
  <li>JWT token is generated</li>
  <li>JWT is stored in the Flutter app</li>
  <li>All protected APIs require the JWT token</li>
</ol>

<hr/>

<h2>🗄️ Vault APIs (Normal Online Usage)</h2>
<p>
Vault APIs are used during <b>normal online usage</b>.
They directly interact with the PostgreSQL database.
</p>

<ul>
  <li><b>Create Entry:</b> <code>POST /vault/entries</code></li>
  <li><b>Get Entries:</b> <code>GET /vault/entries</code></li>
  <li><b>Update Entry:</b> <code>PUT /vault/entries/{entry_id}</code></li>
  <li><b>Delete Entry:</b> <code>DELETE /vault/entries/{entry_id}</code></li>
</ul>

<p><b>Note:</b> Vault APIs always require an active internet connection.</p>

<hr/>

<h2>🔄 Sync APIs (Offline Synchronization)</h2>
<p>
Sync APIs are used when the user makes changes while <b>offline</b>
and needs to synchronize local encrypted data with the server.
</p>

<h3>📤 Sync Push</h3>
<pre><code>POST /sync/push</code></pre>
<ul>
  <li>Deletes old vault data on the server</li>
  <li>Uploads full encrypted local vault</li>
  <li>Replaces server vault with local vault</li>
</ul>

<h3>📥 Sync Pull</h3>
<pre><code>GET /sync/pull</code></pre>
<ul>
  <li>Fetches latest vault data from server</li>
  <li>Updates local encrypted storage in Flutter</li>
</ul>

<hr/>

<h2>🆚 Vault APIs vs Sync APIs</h2>

<table border="1" cellpadding="8">
  <tr>
    <th>Feature</th>
    <th>Vault APIs</th>
    <th>Sync APIs</th>
  </tr>
  <tr>
    <td>Purpose</td>
    <td>Normal CRUD operations</td>
    <td>Offline synchronization</td>
  </tr>
  <tr>
    <td>Internet Required</td>
    <td>Yes</td>
    <td>Yes (after offline)</td>
  </tr>
  <tr>
    <td>Data Source</td>
    <td>PostgreSQL DB</td>
    <td>Local encrypted storage</td>
  </tr>
  <tr>
    <td>Frequency</td>
    <td>Frequent</td>
    <td>Occasional</td>
  </tr>
  <tr>
    <td>Operation Scope</td>
    <td>Single entry</td>
    <td>Entire vault</td>
  </tr>
</table>

<hr/>

<h2>📱 Offline Mode (Flutter)</h2>
<ul>
  <li>When offline, Flutter uses <b>local encrypted storage</b></li>
  <li>CRUD operations happen locally</li>
  <li>When internet is restored:
    <ul>
      <li>Sync Push is called</li>
      <li>Sync Pull is called</li>
    </ul>
  </li>
</ul>

<hr/>

<h2>🧠 Device Support (Future Enhancement)</h2>
<p>
Device tracking can be added in future to support:
</p>
<ul>
  <li>Multiple device sync</li>
  <li>Last sync timestamps</li>
  <li>Device-level security</li>
</ul>

<p><b>Current version works without device tracking.</b></p>

<hr/>

<h2>🧪 API Testing</h2>
<ol>
  <li>Run the server:
    <pre><code>uvicorn app.main:app --reload</code></pre>
  </li>
  <li>Open Swagger UI:
    <pre><code>http://127.0.0.1:8000/docs</code></pre>
  </li>
</ol>

<hr/>

<h2>🛡️ Security Design</h2>
<ul>
  <li>Passwords are never stored in plain text</li>
  <li>Passwords are hashed using bcrypt</li>
  <li>Vault data is encrypted before storage</li>
  <li>JWT protects all sensitive routes</li>
</ul>

<hr/>

<h2>🎓 Viva Explanation</h2>
<blockquote>
  Vault APIs handle normal online CRUD operations, while Sync APIs
  synchronize offline encrypted data with the server when internet is restored.
</blockquote>

<hr/>

<h2>✅ Project Status</h2>
<ul>
  <li>✔ Authentication implemented</li>
  <li>✔ Vault APIs implemented</li>
  <li>✔ Sync APIs implemented</li>
  <li>✔ Offline-first design</li>
  <li>⏳ Device support (future)</li>
</ul>
