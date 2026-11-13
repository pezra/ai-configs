# API and service reference

## 9. Genre playbook (excerpt)

**API / service reference.** `fieldName (type, constraint) - description.` per field. One sentence per definition unless the term is genuinely surprising. Inline code everywhere a name appears.

## 10. Rewrites (excerpt)

**First-person narration → impersonal spec.**
> *Before:* I decided that the payable amount for an account shouldn't live with the account record itself, since we already have a service that tracks balances, so I made it pull from there instead.
>
> *After:* Unlike invoices and other payable categories, the payable amount of an account is maintained in a separate service.

The system is the subject; the reasoning that produced the decision isn't restated, just the result.

**Teacherly gloss → reference entry.**
> *Before:* A KRN, or KUBRA Resource Name, is basically our version of a URN — it's a string that uniquely identifies a resource, kind of like a primary key but portable across services.
>
> *After:* `accountNumber (string, required) - the utility's account number.`
>
> KRNs are names, not locators. They are not inherently dereferenceable — you cannot retrieve a representation of the identified resource using just the KRN.

Definition given as a field entry or a flat declarative, not a guided explanation; the term is assumed, then one clarifying fact follows.
