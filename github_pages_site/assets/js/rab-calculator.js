/* ==========================================================================
   INTERACTIVE RAB CALCULATOR LOGIC FOR INCAP WEBSITE
   ========================================================================== */

function calculateRAB() {
    const solusiType = document.getElementById('solusi-type').value;
    const modulAi = document.getElementById('modul-ai').checked;
    const modulSec = document.getElementById('modul-sec').checked;
    const modulIot = document.getElementById('modul-iot').checked;
    const scaleTier = document.getElementById('scale-tier').value;

    let baseTimelineWeeks = 4;
    let teamComposition = ['Solution Architect', 'Fullstack Software Engineer'];
    let keyDeliverables = ['Arsitektur Sistem & Source Code', 'Dokumentasi PoC & Manual User'];

    // Solution base logic
    if (solusiType === 'web') {
        baseTimelineWeeks += 2;
        teamComposition.push('Frontend & Backend Specialist');
        keyDeliverables.push('Rest API & Microservices Container');
    } else if (solusiType === 'mobile') {
        baseTimelineWeeks += 3;
        teamComposition.push('Mobile App Developer (Flutter/Native)');
        keyDeliverables.push('Build APK/IPA & Local Encrypted Storage');
    } else if (solusiType === 'security') {
        baseTimelineWeeks += 2;
        teamComposition.push('White Hacker & Security Auditor');
        keyDeliverables.push('Laporan Penetration Testing & OWASP Hardening');
    } else if (solusiType === 'iot') {
        baseTimelineWeeks += 3;
        teamComposition.push('IoT & Embedded Hardware Engineer');
        keyDeliverables.push('Integrasi Protokol MQTT/Modbus & Dashboard Live');
    }

    // Addons
    if (modulAi) {
        baseTimelineWeeks += 2;
        teamComposition.push('AI / Data Scientist');
        keyDeliverables.push('Model ML Trained (Sentiment / Price Prediction)');
    }
    if (modulSec && !teamComposition.includes('White Hacker & Security Auditor')) {
        baseTimelineWeeks += 1;
        teamComposition.push('Security Specialist');
        keyDeliverables.push('White Hacker Audit Phase');
    }
    if (modulIot && !teamComposition.includes('IoT & Embedded Hardware Engineer')) {
        baseTimelineWeeks += 2;
        teamComposition.push('IoT Firmware Specialist');
    }

    // Tier scaling
    let scaleMultiplier = "Standard Scale";
    if (scaleTier === 'medium') {
        baseTimelineWeeks = Math.ceil(baseTimelineWeeks * 1.3);
        scaleMultiplier = "Medium Enterprise Tier (1.000 - 50.000 users)";
        teamComposition.push('DevOps Engineer');
    } else if (scaleTier === 'high') {
        baseTimelineWeeks = Math.ceil(baseTimelineWeeks * 1.6);
        scaleMultiplier = "High Availability Scale (> 100.000 users)";
        teamComposition.push('DevOps & Database Administrator (DBA)');
        keyDeliverables.push('Kubernetes Cluster Config & Multi-Region DB Redundancy');
    }

    // Render HTML Output
    const outputContainer = document.getElementById('rab-output');
    const outputContent = document.getElementById('rab-output-content');

    outputContent.innerHTML = `
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 20px;">
            <div style="background: rgba(255,255,255,0.03); padding: 12px; border-radius: 8px;">
                <span style="font-size: 0.8rem; color: #8892b0; display: block;">Estimasi Waktu Pengerjaan:</span>
                <strong style="font-size: 1.4rem; color: #00f2fe;">${baseTimelineWeeks} - ${baseTimelineWeeks + 2} Minggu</strong>
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 12px; border-radius: 8px;">
                <span style="font-size: 0.8rem; color: #8892b0; display: block;">Tingkat Skala Sistem:</span>
                <strong style="font-size: 1rem; color: #4facfe;">${scaleMultiplier}</strong>
            </div>
        </div>

        <h5 style="color: #00f2fe; margin-bottom: 8px; font-size: 1rem;">👥 Tim Spesialis INCAP yang Dialokasikan:</h5>
        <ul style="list-style: square; padding-left: 20px; color: #a8b2d1; margin-bottom: 16px; font-size: 0.9rem;">
            ${teamComposition.map(role => `<li>${role}</li>`).join('')}
        </ul>

        <h5 style="color: #00f2fe; margin-bottom: 8px; font-size: 1rem;">📦 Deliverables Utama:</h5>
        <ul style="list-style: square; padding-left: 20px; color: #a8b2d1; margin-bottom: 20px; font-size: 0.9rem;">
            ${keyDeliverables.map(item => `<li>${item}</li>`).join('')}
        </ul>

        <div style="background: rgba(0, 242, 254, 0.08); border-left: 3px solid #00f2fe; padding: 12px; border-radius: 4px; font-size: 0.85rem; color: #e6f1ff;">
            💡 <strong>RAB Transparan & Uji PoC:</strong> Setiap estimasi akan dikonfirmasi melalui tahapan <em>Proof of Concept (PoC)</em> berbasis bukti nilai bisnis terlebih dahulu sebelum kesepakatan produksi.
        </div>
    `;

    outputContainer.classList.remove('hidden');
    outputContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
