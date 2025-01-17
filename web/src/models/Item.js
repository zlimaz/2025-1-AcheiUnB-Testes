export default class Item {
  constructor(
    user = null,
    name = "",
    category = null,
    location = null,
    color = null,
    brand = null,
    description = null,
    images = null,
    status = "",
    foundLostDate = "",
    createdAt = new Date(),
    barcode = "",
    requiredFields = [
      "name",
      "category",
      "location",
      "color",
      "brand",
      "description",
      "status",
      "foundLostDate",
    ]
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
