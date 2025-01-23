export default class Item {
  constructor(
    user = null,
    name = "",
    category = "",
    location = "",
    color = "",
    foundLostDate = "",
    brand = "",
    description = null,
    images = null,
    status = "",
    createdAt = new Date(),
    barcode = "",
    requiredFields = ["name", "category", "location"]
  ) {
    this.user = user;
    this.name = name;
    this.category = category;
    this.location = location;
    this.color = color;
    this.brand = brand;
    this.description = description;
    this.images = images;
    this.status = status;
    this.foundLostDate = foundLostDate;
    this.createdAt = createdAt;
    this.barcode = barcode;
    this.requiredFields = requiredFields;
  }
}
