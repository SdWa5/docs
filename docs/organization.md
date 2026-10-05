# SdWa5 — Organization

Official / legal information for the SdWa5 organization.

## Legal identity

| Field       | Value                                        |
|-------------|-----------------------------------------------|
| Legal name  | Musikverein Schmeiß die Wand an 5             |
| Display name| SdWa5 (Scheiß die Wand an 5)                  |
| Sitz        | Ostermiething (Ostermiething) — move to Hof bei Salzburg pending, see below |
| Zustellanschrift | Egitlweg 6, 5322 Hof bei Salzburg, Österreich (since 2026-09-14) |
| ZVR         | 1115343752                                    |
| Founded (Entstehungsdatum) | 2023-01-05                     |
| Registration authority | Bezirkshauptmannschaft Braunau — changes with the Sitz |
| Domain      | sdwa5.org                                     |
| Tax status  | Kleinunternehmer §6 Abs. 1 Z 27 UStG (no VAT) |

Source for everything except the Zustellanschrift: Vereinsregisterauszug zum
Stichtag 2026-07-04. A current extract can always be fetched from the
[public ZVR register](https://citizen.bmi.gv.at/at.gv.bmi.fnsweb-p/zvn/public/Registerauszug)
(ZVR 1115343752); older extracts in the
[Google Drive folder](https://drive.google.com/drive/folders/1deC0DDdF5bXz1OuGvVQTcvSgrui9EpmV);
Shopware Impressum config, see
[`sdwa5-vps/docs/shopware/shop-config.md`](../sdwa5-vps/docs/shopware/shop-config.md#shop-identity)
and [`sdwa5-vps/docs/caddy.md`](../sdwa5-vps/docs/caddy.md).

### Address change, in progress since 2026-09-14

The postal address and the Sitz move separately, and only the first has
happened. Do not read the table as one event.

- **Zustellanschrift.** Changed to Egitlweg 6, 5322 Hof bei Salzburg by
  resolution of the Vorstand on 2026-09-14. A change of the Vereinsanschrift is
  a notification to the Vereinsbehörde under § 14 Abs 3 VerG, due within four
  weeks and free of charge. Until the notification is processed, the ZVR extract
  still shows the old address, so an extract that contradicts this table is
  not necessarily out of date — it may simply be ahead of the filing.
- **Sitz.** Still Ostermiething, because § 1 Abs 2 of the statutes names it and
  changing it is a Statutenänderung under § 14 Abs 1 VerG: a two-thirds
  resolution of the Generalversammlung, then a notification the authority has
  four weeks to forbid, extendable to six. Fee roughly 21 € plus 6 € per page of
  the attached statutes.
- **Competent authority.** Bezirkshauptmannschaft Braunau am Inn today, because
  competence follows the Sitz and Ostermiething is in Oberösterreich. Both
  notifications therefore go to Braunau, not to Salzburg. Once the Sitz move is
  registered, competence passes to Bezirkshauptmannschaft Salzburg-Umgebung,
  Dr.-Hans-Katschthaler-Platz 1, 5201 Seekirchen am Wallersee.
- **Place of jurisdiction** in the storefront AGB follows the Sitz, so it stays
  Ostermiething until the move is registered.

Egitlweg 6 is also the private address of a board member and of one other
member. It is in this repository in plain text on purpose: § 5 ECG obliges the
Verein to publish the same address in its Impressum, and the ZVR extract is
public, so withholding it here would hide nothing.

## Board (Vorstand)

Per statutes: Vorstand = 3 members (Obmann + 2 Stellvertreter). No Kassier/Schriftführer roles.
Funktionsperiode: 5 years, current 2022-10-27 – 2027-10-26.

| Role                     | Name                | Since      |
|--------------------------|---------------------|------------|
| Obmann                   | Stefan Ripper       | 2022-10-27 |
| Obmann-Stellvertreterin  | see ZVR register    | 2024-04-18 |
| Obmann-Stellvertreter    | see ZVR register    | 2022-10-27 |

History: the previous Obmann-Stellvertreterin (2022-10-27 – 2024) left
the Verein; a replacement was elected in the Generalversammlung
(Wahlanzeige § 14 Abs 2 VerG, filed 2024-04-18).

Vertretungsregelung: Obmann represents the Verein externally. Written documents
require signatures of Obmann **and** one Stellvertreter to be valid. If Obmann
is unavailable, Stellvertreter act in his place.

## Rechnungsprüfer

| # | Name             |
|---|------------------|
| 1 | Stefan Ripper    |
| 2 | see ZVR register |

Note: statutes § 13 say Rechnungsprüfer must not belong to an organ whose
activity they audit, and both hold Vorstand roles. Unresolved conflict, and it
belongs in the same amendment as the four defects recorded in
[statuten.md](statuten.md). Stated by role rather than against a person,
decided 2026-09-15: the defect is the association's, not any individual's.

## Bank / payments

PayPal: mail@sdwa5.org, https://paypal.me/SdWa5, handle `@SdWa5`.
No bank IBAN.

Revolut Business was ruled out on 2026-10-05, because it does not accept a Verein in DACH. The
PayPal account is being connected to Dolibarr instead, see [services.md](services.md#paypal).

PayPal alone leaves two gaps open, recorded on 2026-10-05 as proposals for the Vorstand.

- **SEPA and IBAN.** PayPal cannot pay to a third party's IBAN and cannot collect through a normal
  SEPA mandate. An invoice that offers only a bank transfer is paid privately by a member and
  becomes an advance, membership fees cannot be debited, and money that arrives only by bank
  transfer, such as sponsorship or public funding, has no account to arrive on.
- **Cards.** Shops that take only cards, deposits and pre-authorisations, and card payments at
  events are not covered. The PayPal Business Debit Mastercard and Zettle would land in the same
  PayPal account, and neither has been checked for this account yet.

Both gaps point to an Austrian Vereinskonto. finanzinfo.at (as of 2026-08-17) puts Austrian price
lists between 10.76 € a quarter and 23.49 € a month, and collecting SEPA direct debits also needs a
creditor ID and a collection agreement with the bank. Comparing three concrete offers would take
ca. 1 Stunde.

## Statutes (Vereinsstatuten)

Full text as a reading copy: [`statuten.md`](statuten.md). The authoritative
version stays the stamped scan `Statuten_Stempel.pdf` in the
[Google Drive folder](https://drive.google.com/drive/folders/1deC0DDdF5bXz1OuGvVQTcvSgrui9EpmV),
next to the `Vereinsstatuten.docx` the reading copy was converted from.

`statuten.md` also lists four defects in the filed version, from an unfilled
template line in § 1 Abs. 3 to three internal cross-references that point one
paragraph too high. They matter for the planned Sitz change, because amending
the statutes reopens the whole document for the authority's review.

Key points:

- Purpose: non-profit; spaces for artistic/musical development, organizing
  musical events. Activity area: Europe.
- Funds: membership fees, event revenue, donations.
- Organs: Generalversammlung, Vorstand (3 members, 5-year term),
  2 Rechnungsprüfer (5-year term), Schiedsgericht (3 members, ad hoc).
- Generalversammlung: annual; invitations ≥1 week ahead (written + digital);
  motions ≥3 days ahead; quorum regardless of attendance; statute changes /
  dissolution need 2/3 majority.
- Dissolution: only by Vorstand, absolute majority; remaining assets go to an
  organization with same/similar purpose, else social welfare.

## Documents

All org documents live in the
[Google Drive folder](https://drive.google.com/drive/folders/1deC0DDdF5bXz1OuGvVQTcvSgrui9EpmV):
Vereinsstatuten, Vereinsregisterauszug, Wahlanzeige, etc.
