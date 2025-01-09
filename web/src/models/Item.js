export default class Item {
  constructor({
    user = null,
    name = "",
    description = "",
    category = null,
    location = "",
    color = null,
    brand = null,
    isValuable = false,
    status = "lost",
    foundLostDate = null,
    createdAt = new Date(),
    barcode = undefined,
  }) {
    this.user = user;
    this.name = name;
    this.description = description;
    this.category = category;
    this.location = location;
    this.color = color;
    this.brand = brand;
    this.isValuable = isValuable;
    this.status = status;
    this.foundLostDate = foundLostDate;
    this.createdAt = createdAt;
    this.barcode = barcode;
  }
}
